import sys

from PySide6.QtGui import (
    QIcon,
    QAction
)
from PySide6.QtWidgets import (
    QApplication,
    QMenu
)

from src.ui.windows.ui_main_window import UIMainWindow
from src.ui.splash import show_splash
from project_info import Info


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
        self.app_window.splash.finish(self.app_window)
        self.app_window.show()

        self.app_window.tray.setIcon(QIcon(Info.ICON_PATH))
        self.app_window.tray.setVisible(True)
        self.app_window.tray.setToolTip(Info.PROJECT_TITLE)

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
        menu_item2.triggered.connect(show_splash)
        self.app_window.tray.activated.connect(self.app_window.show)

        sys.exit(self.app.exec())

    def change_theme(self) -> None:
        self.app_window.signal_theme_changed.emit(self.app)

    def change_app_stay_open(self) -> None:
        self.app_window.signal_app_stay_open_changed.emit(self.app)


if __name__ == '__main__':
    Main().main()
