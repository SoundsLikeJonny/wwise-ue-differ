import dataclasses


@dataclasses.dataclass
class Info:
    NOTIFICATION_TIME: int = 50
    PROJECT_TITLE: str = 'Wwise Unreal AkEvent Differ'
    COMPANY: str = 'Otherside Entertainment'
    RESOURCES_PATH: str = 'resources'
    ICON_PATH: str = f'{RESOURCES_PATH}/ose_favicon.png'
    SPLASH_PATH: str = f'{RESOURCES_PATH}/otherside-logo.png'
    DOCS_LINK: str = 'https://otherside.atlassian.net/wiki/spaces/TVT/pages/3372482581/Wwise+Unreal+AkEvent+Differ'


@dataclasses.dataclass
class FileTypes:
    PROJECT: str = '.wwuedif'
    DATA: str = '.dif_dat'
    PREFS: str = '.prefs'

    ALL_TYPES: tuple = (
        PROJECT,
        DATA,
        PREFS
    )

    @staticmethod
    def is_type_in_file(file: str):
        for extension in FileTypes.ALL_TYPES:
            if file.endswith(extension):
                return True
        return False
