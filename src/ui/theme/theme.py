#  Copyright (c) 2024 Jon Evans.
#
#  The original Wwise-Python Tool Template and source code is provided by Jon Evans,
#  Copyright 2024 (c) Jon Evans Audio under the Apache License, Version 2.0
#  for the purposes of distributing internal tools
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

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet, list_themes


def set_default_theme(app: QApplication):
    app.setStyleSheet('')


def set_ose_theme(app: QApplication):
    apply_stylesheet(app, theme='dark_cyan.xml', extra=Defaults.EXTRA)


class Defaults:
    EXTRA = {'density_scale': '-2'}
