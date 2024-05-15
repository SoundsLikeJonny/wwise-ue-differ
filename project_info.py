import dataclasses


@dataclasses.dataclass
class Info:
    NOTIFICATION_TIME: int = 50
    PROJECT_TITLE: str = 'Wwise Unreal AkEvent Differ'
    COMPANY: str = 'Otherside Entertainment'
    COPYRIGHT: str = 'Copyright (c) Otherside Entertainment 2024'
    NOTICE: str = 'Original Wwise-Python Tool template provided by Jon Evans, Game Audio Tools.'
    RESOURCES_PATH: str = 'resources'
    ICON_PATH: str = f':/{RESOURCES_PATH}/ose_favicon.png'
    SPLASH_PATH: str = f':/{RESOURCES_PATH}/ose_splash.png'
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
