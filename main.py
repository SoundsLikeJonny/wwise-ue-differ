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

import sys

from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtGui import (
    QIcon,
    QAction
)
from PySide6.QtWidgets import (
    QApplication,
    QMenu, QMainWindow
)

from src.ui.windows.ui_main_window import UIMainWindow
from src.ui.splash import SplashScreen
from project_info import Info
import resources


class Main:

    def __init__(self):
        self.app: QApplication | None = None
        self.app_window: UIMainWindow | None = None

    def main(self):
        self.app = QApplication()

        self.app_window = UIMainWindow()
        self.app_window.actionQuit.triggered.connect(self.app.quit)
        self.app_window.radioButton_theme_ose.toggled.connect(self.change_theme)
        self.app_window.signal_theme_changed.emit(self.app)
        self.app_window.signal_app_stay_open_changed.emit(self.app)
        self.app_window.checkBox_keep_app_open.stateChanged.connect(self.change_app_stay_open)
        self.app_window.signal_splash_screen_closed.connect(self.show_window)
        self.app_window.tray.setIcon(QIcon(Info.ICON_PATH))
        self.app_window.tray.setVisible(True)
        self.app_window.tray.setToolTip(Info.PROJECT_TITLE)
        self.app_window.splash.splash_screen.finish(self.app_window)
        self.app_window.show()

        menu = QMenu()
        menu_item1 = QAction("Show Window")
        menu_item2 = QAction("Info")
        menu.addAction(menu_item1)
        menu.addAction(menu_item2)

        quit_app = QAction("Quit")
        quit_app.triggered.connect(self.app.quit)
        menu.addAction(quit_app)

        self.app_window.tray.setContextMenu(menu)

        menu_item1.triggered.connect(self.app_window.show)
        menu_item2.triggered.connect(SplashScreen)
        self.app_window.tray.activated.connect(self.app_window.show)

        sys.exit(self.app.exec())

    def change_theme(self) -> None:
        self.app_window.signal_theme_changed.emit(self.app)

    def change_app_stay_open(self) -> None:
        self.app_window.signal_app_stay_open_changed.emit(self.app)

    @Slot(UIMainWindow)
    def show_window(self):
        self.app_window.show()


if __name__ == '__main__':
    Main().main()
