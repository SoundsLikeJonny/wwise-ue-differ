from typing import Dict, Any, List
from waapi import WaapiClient, CannotConnectToWaapiException


class WAAPI(WaapiClient):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('WAAPI initialised')

    def __del__(self):
        self.disconnect()
        print('WAAPI closed safely')

    def get_project_info(self) -> dict:
        return self.call('ak.wwise.core.getProjectInfo')

    def get_originals_path(self) -> str:
        return self.get_project_info()['directories']['originals']

    def get_root_path(self) -> str:
        return self.get_project_info()['directories']['root']

    def get_languages(self):
        return self.get_project_info()['languages']

    def get_topics(self) -> dict:
        return self.call('ak.wwise.waapi.getTopics')

    def bring_wwise_ui_to_foreground(self) -> dict:
        return self.call('ak.wwise.ui.bringToForeground')

    def get_connection_status(self) -> dict:
        return self.call('ak.wwise.core.remote.getConnectionStatus')

    def is_type(self, guid: str, w_type: str) -> bool:
        result = self.get_waql(f'$ from object "{guid}"')
        print(result)
        return result['return'][0]['type'] == w_type

    def is_sound(self, guid: str) -> bool:
        return self.is_type(guid, 'Sound')

    def get_waql(self, waql_string, return_list: list = None) -> dict:
        if return_list == None:
            return_list = Defaults.DEFAULT_WWISE_ACCESSORS

        object_args = {
            "waql": waql_string,
            "options": {
                "return": return_list
            }
        }

        return self.call('ak.wwise.core.object.get', object_args)

    def get_physical_folder_work_units(self) -> dict:
        return self.get_waql('$ from project where workunitType = "folder"')['return']

    def get_physical_folder_work_units_name_list(self) -> list:
        data_dict = self.get_physical_folder_work_units()
        return [item['name'] for item in data_dict]

    def get_event_guid_from_name(self, event_name: str) -> str:
        if (result := self.get_waql(f'$ from object "Event:{event_name}"')) is not None:
            return result['return'][0]['id']
        return ''

    def delete_event(self, event: str) -> None:
        object_args = {
            "object": event
        }
        self.call('ak.wwise.core.object.delete', object_args)

    def get_actor_mixer_workunits(self):
        return self.get_waql('$ from object "Actor-Mixer Hierarchy" select children')

    def get_wwise_object_from_path(self, path: str):
        return self.get_waql(f'$ from object "{path}" select this')

    def select_wwise_object_from_path(self, path: str):
        return self.execute_command(command='FindInProjectExplorerSyncGroup1', objects=[path])

    def get_actor_mixers(self):

        object_args = {
            "waql": '$ from object "Actor-Mixer Hierarchy" select children select children',
            "options": {
                "return": ["id", "name", "type"]
            }
        }

        return self.call('ak.wwise.core.object.get', object_args)['return']

    def get_guid_actor_mixer_hierarchy(self) -> str:
        return self.get_guid_from_hierarchy_name('Actor-Mixer Hierarchy')

    def get_guid_events_hierarchy(self) -> str:
        return self.get_guid_from_hierarchy_name('Events')

    def get_guid_soundbanks_hierarchy(self) -> str:
        return self.get_guid_from_hierarchy_name('SoundBanks')

    def get_guid_from_hierarchy_name(self, name: str) -> str:
        result = self.get_waql(f'$ from object "{name}"')
        if result:
            result = result['return'][0]
            result = result['id']
            return result
        return ''

    def include_event_in_soundbank(self, soundbank: str, event: str) -> dict:
        args = {
            "soundbank": soundbank,
            "operation": 'add',
            "inclusions": [
                {
                    "object": event,
                    "filter": [
                        "events",
                        "structures"
                    ]
                }
            ]
        }
        return self.call('ak.wwise.core.soundbank.setInclusions', args)

    def get_action_from_event(self, event_name: str) -> list[dict[str, str, str]]:
        """

        :param event_path:
        :return: Action id
        """

        if (result := self.get_waql(f'$ from object "Event:{event_name}" select children')) is not None:
            return result['return']
        return None

        # return self.get_waql(f'$ from object "{E8209C12-5272-46A8-8757-CD4E986CD9DB}"')['return']

    def get_target_from_action(self, action_id):
        result = self.get_waql(f'$ from object "{action_id}" select target')
        if result is not None and result['return']:
            print(result)
            return result['return'][0]
        return {}

    def import_files_to_wwise(self, audio_file_path: str, import_location: str = None, import_language="SFX",
                              name: str = '', originals_sub_folder: str = '',
                              import_operation: str = 'createNew') -> dict:

        if not import_location:
            import_location = ''

        parent_path = self.get_parent_path_from_guid(import_location)
        parent_path = parent_path + f'\\<Sound>{name}'
        print('parent_path', parent_path)

        args = {

            "importOperation": import_operation,
            "default": {
                "importLanguage": import_language,
                "importLocation": import_location,
                "audioFile": audio_file_path,
                'originalsSubFolder': originals_sub_folder,
                'objectType': 'Sound',
            },
            'imports': [
                {
                    'objectPath': ''
                }
            ],
            "autoAddToSourceControl": True,
            # "imports": audio_import_list,
        }

        return self.call('ak.wwise.core.audio.import', args)

    def create_action_in_event(self, parent: str, target: dict):
        target = self.get_sound_from_object_list(target)

        args = {
            "@ActionType": 1,
            "@Target": target
        }
        self.create_object(parent, 'Action', '', args=args)

    def get_sound_from_object_list(self, target):
        sound_guid: list = []
        for item in target['objects']:
            if self.is_sound(item['id']):
                sound_guid.append(item['id'])
        target: str = sound_guid[0]
        return target

    def create_object(self, parent: str, ttype: str, name: str, args: dict = None, on_conflict: str = 'merge') -> dict:

        object_args = {
            "parent": parent,
            "type": ttype,
            "name": name,
            "autoAddToSourceControl": True,
            "onNameConflict": on_conflict
        }

        if args is not None and isinstance(args, dict):
            object_args.update(args)
            print(f'object_args: {object_args}')

        result = self.call('ak.wwise.core.object.create', object_args)
        return result

    def create_work_unit_in_actor_mixer_hierarchy(self, new_work_unit_name: str) -> dict:
        parent = self.get_actor_mixer_hierarchy_guid()
        return self.create_object(parent, Defaults.WORK_UNIT, new_work_unit_name)

    def get_parent(self, current_object_guid: str) -> dict:

        object_args = {
            "waql": f'$ from object "{current_object_guid}" select parent',
            "options": {
                "return": ["id", "name", "type"]
            }
        }
        return self.call('ak.wwise.core.object.get', object_args)

    def get_guid_from_json(self, json_dict: dict) -> str:
        return json_dict['id']

    def get_name_from_json(self, json_dict: dict) -> str:
        return json_dict['name']

    def get_type_from_json(self, json_dict: dict) -> str:
        return json_dict['type']

    def checkout_workgroup_wav(self) -> None:
        object_guids = self.get_selected_object_guids()
        self.execute_command('WorkgroupCheckoutWAV', object_guids)

    def execute_command(self, command: str, objects: list) -> None:
        args = {
            'command': command,
            'objects': objects
        }
        self.call('ak.wwise.ui.commands.execute', args)

    def get_recursive_list_of_children(self, list_of_children: list, index=0) -> dict[str, str | Any]:
        object_type_list = [Defaults.WORK_UNIT, Defaults.ACTOR_MIXER, Defaults.SWITCH_CONTAINER, Defaults.SEQUENCE]
        current_type = Defaults.SEQUENCE

        if index < len(object_type_list):
            current_list_item = list_of_children[index]
            current_type = object_type_list[index]

            index = index + 1

            return {
                "type": current_type,
                "name": current_list_item,
                'children': self.get_list_of_children_to_create_from_list(list_of_children, index=index)
            }

        else:
            return {}
        # [] ??

    def create_all_children_objects(self, parent: str, type: str, name: str, list_of_children: list) -> dict:
        list_of_children = self.get_recursive_list_of_children(list_of_children)

        parent = self.get_actor_mixer_hierarchy_guid()
        type = "WorkUnit"
        name = "Player"

        object_args = {
            "parent": parent,
            "type": type,
            "name": name,
            "autoAddToSourceControl": True,
            "children": list_of_children,
            "onNameConflict": "merge"
        }

        result = self.call('ak.wwise.core.object.create', object_args)
        return result

    def create_objects_from_path(self, list_of_children: list) -> None:
        object_type_list = [Defaults.ACTOR_MIXER, Defaults.SWITCH_CONTAINER, Defaults.FOLDER, Defaults.SEQUENCE,
                            Defaults.FOLDER]
        current_object_type = object_type_list[0]

        list_of_children.insert(0, Defaults.DFAULT_PARENT_FOLDER)
        end_object = list_of_children[-1:][0]
        list_of_children = list_of_children[:-1]

        new_list = [f'\\<{object_type_list[index]}>{item}' for index, item in enumerate(list_of_children)]

        path = ''.join(new_list)

        self.create_object(path, Defaults.FOLDER, end_object)

    def create_new_object_tree(self, filename_list: list) -> dict:

        object_type_list = [Defaults.ACTOR_MIXER, Defaults.SWITCH_CONTAINER, Defaults.SEQUENCE]
        current_object_type = object_type_list[0]
        current_parent_object = self.get_actor_mixer_hierarchy_guid()

        for index, item in enumerate(filename_list):

            # Set the current obejct type for scope
            if index < len(object_type_list):
                current_object_type = object_type_list[index]

                found_actor_bool = False
                actor_mixers_all = self.get_actor_mixers()

                #
                for actor_mixer in actor_mixers_all:
                    # First check that there exists an actor mixer with the same name as item,
                    # or that the actor mixer name is partially in the item
                    if item == actor_mixer['name'] or actor_mixer['name'] in item:
                        found_actor_bool = True
                        current_parent_object = actor_mixer['id']


                    # If the existing actor mixer name partially matches the current item in the list filename_list,
                    # then 
                    elif actor_mixer['name'] in item and not item == actor_mixer['name']:
                        found_actor_bool = True
                        current_parent_object = actor_mixer['id']
                        new_actor_mixer = self.create_object(current_parent_object, Defaults.ACTOR_MIXER, item)
                        current_parent_object = self.get_guid_from_json(new_actor_mixer)

                # Create the tree if no actor mixer found
                if not found_actor_bool:
                    new_work_unit = self.create_work_unit_in_actor_mixer_hierarchy(item)
                    work_unit_id = self.get_guid_from_json(new_work_unit)

                    new_actor_mixer = self.create_object(work_unit_id, Defaults.ACTOR_MIXER, item)
                    new_actor_mixer = self.get_guid_from_json(new_actor_mixer)
                    current_parent_object = new_actor_mixer['id']

            # print(index)
        return False

    def create_switches_under_path_from_selected_object_names(self):
        path = ''
        object_type = ''
        self.create_objects_under_path_from_selected_object_names(path, object_type)

    def get_all_switch_groups(self) -> dict:
        return_list = Defaults.DEFAULT_WWISE_ACCESSORS.append('path')
        type = 'SwitchGroup'
        return self.get_all_objects_of_type(return_list, type=type)

    def get_all_switch_groups_names(self) -> list:
        switch_groups = self.get_all_switch_groups()
        switch_groups = [item['name'] for item in switch_groups]

    def get_all_switch_groups_guids(self) -> list:
        switch_groups = self.get_all_switch_groups()
        switch_groups = [item['id'] for item in switch_groups]

    def get_all_switch_groups_paths(self) -> list:
        switch_groups = self.get_all_switch_groups()
        return [item['path'] for item in switch_groups]

    # TODO: clear errors
    # TODO: make non-test
    def get_property_info(self) -> dict:
        args = {
            'objects': '\\Switches\\Player\\StatusEffects\\SWG_Player_StatusEffect'
        }
        return self.call('ak.wwise.core.object.getPropertyInfo', args)

    def set_property(self, w_object: str, w_property: str, value: Any):
        args = {
            'object': w_object,
            'property': w_property,
            'value': value
        }
        return self.call('ak.wwise.core.object.setProperty', args)

    def create_switches_from_object_name_list(self, name_list: list, switch_group_path: str) -> None:
        for item in name_list:
            self.create_object(switch_group_path, 'Switch', item)

    def get_selected_objects(self) -> list:
        if self.is_connected():
            return self.call('ak.wwise.ui.getSelectedObjects', WArguments.DEFAULT)
        else:
            return None

    def get_selected_object_guids(self) -> list:
        objects_list = self.get_selected_objects()
        objects_list = objects_list['objects']
        return [obj['id'] for obj in objects_list]

    def get_selected_object_names(self) -> list:
        if self.is_connected():
            objects_list = self.get_selected_objects()
            objects_list = objects_list['objects']

            return [obj['name'] for obj in objects_list]

        else:
            return None

    def get_selected_object_names_as_string(self):
        if not self.is_connected():
            return None

        name_list = self.get_selected_object_names()

        if len(name_list) == 1:
            return ''.join(name_list)
        elif len(name_list) > 1:
            return ', '.join(name_list)
        else:
            return ''

    def get_selected_object_names_as_string_block(self):
        if not self.is_connected():
            return None

        name_list = self.get_selected_object_names()

        if len(name_list) == 1:
            return ''.join(name_list)
        elif len(name_list) > 1:
            return '\n'.join(name_list)
        else:
            return ''

    def rename_selected_objects(self, new_name: str) -> None:
        guids = self.get_selected_object_guids()

        if not self.is_list_empty(guids):
            if self.is_list_len_multi(guids):

                for index, id in enumerate(guids):
                    pad = self.get_zfill_underscore(index + 1)
                    padded_new_name = f'{new_name}{pad}'
                    self.rename_object(id, padded_new_name)

            else:
                self.rename_object(guids[0], new_name)

    def rename_object(self, guid: str, new_name: str) -> None:
        self.call('ak.wwise.core.object.setName', self.get_rename_args(guid, new_name))

    def get_rename_args(self, guid: str, new_name: str) -> dict[str, str]:
        return {
            "object": guid,
            "value": new_name
        }

    def get_zfill_underscore(self, number: int) -> str:
        pad = str(number).zfill(2)
        return f'_{pad}'

    def get_wwise_object_types_list(self) -> list:
        types = Defaults.OBJECT_LIST
        types.sort()
        return types

    def get_wwise_object_type_icon_dict(self) -> dict:
        types = Defaults.ICONS_DICT
        return types

    def is_list_len_multi(self, list: list) -> bool:
        return len(list) > 1

    def is_list_empty(self, list: list) -> bool:
        return len(list) == 0

    def get_containers_interface(self):
        return Defaults

    def get_parent_path_from_guid(self, guid: str):
        result: dict = self.get_waql(f'$ from object "{guid}"', return_list=['path'])
        # result: dict = self.get_waql(f'$ from object "{guid}"')
        if result:
            result: str = result['return'][0]['path']
            return result
        else:
            return None

    def get_all_wav_files_of_container_descendants(self, container_id) -> list:
        accessor = 'sound:originalWavFilePath'
        return_list = Defaults.DEFAULT_WWISE_ACCESSORS.append(accessor)
        sound_objects = \
            self.get_waql(
                f'$ from object "{container_id}" select descendants where type = "sound"',
                return_list
            )
        if sound_objects is not None:
            return [item[accessor] for item in sound_objects['return'] if accessor in item.keys()]
        return []

    def get_all_wav_file_paths(self):
        return self.get_list_of_sound_objects_filtered_from_accessor('sound:originalWavFilePath')

    def get_list_of_sound_objects_filtered_from_accessor(self, accessor: str) -> list:
        sound_objects = self.get_all_sound_objects(accessor)
        return [item[accessor] for item in sound_objects if accessor in item.keys()]

    def get_all_sound_objects(self, additional_accessor=None):
        return self.get_all_objects_of_type_with_accessor('Sound', additional_accessor)

    def get_all_event_objects(self, additional_accessor=None):
        return self.get_all_objects_of_type_with_accessor('Event', additional_accessor)

    def get_all_objects_of_type_with_accessor(self, type: str, additional_accessor: str = None):

        if additional_accessor != None:
            return_list = Defaults.DEFAULT_WWISE_ACCESSORS.append(additional_accessor)
        else:
            return_list = Defaults.DEFAULT_WWISE_ACCESSORS

        return self.get_all_objects_of_type(return_list, type=type)

    def get_all_objects_of_type(self, return_list: list, type: str = None):
        if type == None:
            type = 'Sound'
        if return_list == None:
            return_list = Defaults.DEFAULT_WWISE_ACCESSORS

        return self.get_waql(f'$ from project where type = "{type}"', return_list)['return']


class Defaults:
    DFAULT_PARENT_FOLDER = 'Actor-Mixer Hierarchy'

    DEFAULT_WWISE_ACCESSORS = [
        'id',
        'name',
        'type',
    ]

    SEQUENCE = 'RandomSequenceContainer'
    RANDOM = 'RandomContainer'
    SOUND = 'Sound'
    SWITCH_CONTAINER = 'SwitchContainer'
    SWITCH_GROUP = 'SwitchGroup'
    SOUNDBANK = 'SoundBank'
    WORK_UNIT = 'WorkUnit'
    ACTOR_MIXER = 'ActorMixer'
    FOLDER = 'Folder'
    BLEND_CONTAINER = 'BlendContainer'
    EVENT = 'Event'
    DIALOGUE_EVENT = 'DialogueEvent'

    OBJECT_LIST = [
        SEQUENCE,
        RANDOM,
        SOUND,
        SWITCH_CONTAINER,
        WORK_UNIT,
        ACTOR_MIXER,
        FOLDER,
        BLEND_CONTAINER,
        EVENT
    ]

    ICONS_DICT = {
        SEQUENCE: '.\\Resources\\ObjectIcons_RandomContainer_nor.png',
        RANDOM: '.\\Resources\\ObjectIcons_SequenceContainer_nor.png',
        SOUND: '.\\Resources\\ObjectIcons_SoundFX_nor.png',
        SWITCH_CONTAINER: '.\\Resources\\ObjectIcons_SwitchContainer_nor.png',
        WORK_UNIT: '.\\Resources\\ObjectIcons_Workunit_nor.png',
        ACTOR_MIXER: '.\\Resources\\ObjectIcons_ActorMixer_nor.png',
        FOLDER: '.\\Resources\\ObjectIcons_Folder_nor.png',
        BLEND_CONTAINER: '.\\Resources\\ObjectIcons_BlendContainer_nor.png',
        EVENT: '.\\Resources\\ObjectIcons_Event_nor.png'
    }


class WArguments:
    DEFAULT = {
        "options": {
            "return": ["id", "name", "type"]
        }
    }


if __name__ == '__main__':
    wwise = WAAPI()
    # results = wwise.get_actor_mixer_hierarchy_guid()
    results = wwise.get_property_info()
    # pprint(results)
    wwise.__del__()
