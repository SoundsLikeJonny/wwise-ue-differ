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
import base64
import gzip
import ast

from project_info import FileTypes


class ProjectFile:

    @staticmethod
    def save(data: any, filename: str) -> None:
        if not ProjectFile.is_file_type_valid(filename):
            print('Invalid filetype of project')
            print(filename)
            return None

        if isinstance(filename, str):
            data = "[{}]".format(data).encode()
            data = base64.b64encode(data)
            data = gzip.compress(data)
            try:
                open(filename, "wb").write(data)
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def load(filename: str) -> any:
        try:
            data = open(filename, "rb").read()
            data = gzip.decompress(data)
            data = base64.b64decode(data)
            data = ast.literal_eval(data.decode())[0]
        except Exception as e:
            print(e)
            return None

        if not data:
            print('No data to load')
            return None

        return data

    @staticmethod
    def is_file_type_valid(file: str) -> bool:
        if FileTypes.is_type_in_file(file):
            return True
        return False
