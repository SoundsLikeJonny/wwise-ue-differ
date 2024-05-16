#  Copyright 2024 Otherside Entertainment Inc.
#
#  Original Wwise-Python Tool Template provided by Jon Evans under Apache 2.0
#  for the purposes of distributing an internal tool
#  Copyright 2024 Jon Evans Audio
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
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
