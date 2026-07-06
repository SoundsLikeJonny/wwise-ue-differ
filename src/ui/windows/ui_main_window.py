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
import builtins
import glob
import pathlib
import webbrowser
from pathlib import Path
import pandas as pd
import pyperclip
from pandas import DataFrame
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import (
    Qt,
    Slot,
    Signal,
    QThreadPool, QObject,
)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QMainWindow,
    QTreeWidgetItem,
    QFileDialog,
    QSystemTrayIcon,
    QSplashScreen,
    QTreeWidget,
    QStackedWidget,
    QGroupBox,
    QApplication,
    QDialog,
    QVBoxLayout,
    QLabel,
    QListWidgetItem, QDialogButtonBox
)

from ui.theme import theme
from engine.filetype import ProjectFile
from project_info import Info, FileTypes
from src.engine.wwise import (
    WAAPI,
    CannotConnectToWaapiException,
    Defaults
)
from src.ui.gui import MainWindow
from src.ui.splash import SplashScreen
from src.ui.windows.ui_progress_window import ProgressBarWindow
import resources

pathlib.Path().cwd()


class UIMainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    signal_progress_bar_maximum = Signal(int)
    signal_progress_bar_message = Signal(str)
    signal_progress_bar_value = Signal(int)
    signal_hide_progress_bar = Signal()
    signal_show_progress_bar = Signal()
    signal_disable_table = Signal()
    signal_enable_table = Signal()
    signal_theme_changed = Signal(QApplication)
    signal_app_stay_open_changed = Signal(QApplication)
    signal_close_progress_window = Signal()
    signal_splash_screen_closed = Signal()

    def __init__(self, *args) -> None:
        """Initialize the main window, UI elements and necessary objects
        """
        super(UIMainWindow, self).__init__(*args)
        self.confirm: QDialog = QDialog()
        self.ak_event_exclusions: list[str] = []
        self.ak_events_to_delete: list[str] = []
        self.setupUi(self)
        self.threadpool = QThreadPool()

        self.QT_WIDGET_TREE_ITEM_FLAGS: Qt.ItemFlag = (
                Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
        self.DIALOGUE_WORK_UNIT_STR = 'Dialogue'

        self.wav_import_errors: list = []
        self.PREFERENCES_FILE = self.get_prefs_path()
        self.PREFERENCES_OBJECTS = [
            self.checkBox_keep_app_open,
            self.listWidget_ak_events,
            self.stackedWidget,
            self.radioButton_theme_ose,
            self.checkBox_use_persistent_data,
            self.lineEdit_ak_events_folder_in_ue,
            self.checkBox_only_show_invalid,
            self.ak_event_exclusions
        ]

        self.listWidget_ak_events.clear()
        self.listWidget_exclusions.clear()

        self.load_prefs()

        self.notify_on_close: bool = self.checkBox_keep_app_open.isChecked()
        self.splash: SplashScreen = SplashScreen()
        self.splash.signal_splash_screen_closed.connect(self.signal_splash_screen_closed.emit)
        self.tray = QSystemTrayIcon()

        self.setWindowIcon(QIcon(Info.ICON_PATH))
        self.setWindowTitle(Info.PROJECT_TITLE)

        self.progress_window: ProgressBarWindow | None = None
        self.continue_importing = False
        """
        #
        BUTTONS
        #
        """
        self.wwise_status_refresh.pressed.connect(self.init_wwise)
        self.pushButton_to_main_page.pressed.connect(self.open_main_page)
        self.pushButton_browse_select_ak_event_folder.pressed.connect(self.select_unreal_wwise_ak_events_path)
        self.pushButton_diff_against_wwise_project.pressed.connect(self.diff_ue_ak_events_folder_against_wwise_events)
        self.pushButton_copy_list_to_clipboard.setIcon(QPixmap(':/resources/icons8-copy-50.png'))
        self.pushButton_copy_list_to_clipboard.pressed.connect(self.copy_list_to_clipboard)
        self.pushButton_delete_unused_ak_events.pressed.connect(self.confirm_delete_unused_ak_events)
        self.pushButton_to_exclusions_page.pressed.connect(self.open_second_page)
        self.pushButton_go_to_main_page.pressed.connect(self.open_main_page)
        self.pushButton_add_selection_to_exclusions.pressed.connect(self.add_selection_to_exclusions_list)

        """
        #
        ACTIONS
        #
        """
        self.actionInfo.triggered.connect(self.show_splash_screen)
        self.actionSee_documentation.triggered.connect(self.open_documentation_link)
        self.actionPreferences.triggered.connect(self.open_preferences)
        self.actionMain_Window.triggered.connect(self.open_main_page)
        self.actionSave.triggered.connect(self.save_prefs)

        """
        #
        SIGNALS
        #
        """
        self.signal_progress_bar_maximum[int].connect(self.update_progress_bar_maximum)
        self.signal_progress_bar_message[str].connect(self.update_progress_bar_message)
        self.signal_progress_bar_value[int].connect(self.update_progress_bar_value)
        self.signal_hide_progress_bar.connect(self.hide_progress_bar)
        self.signal_show_progress_bar.connect(self.show_progress_bar)
        self.signal_theme_changed[QApplication].connect(self.update_theme)
        self.signal_app_stay_open_changed[QApplication].connect(self.update_app_stay_open)

        """
        #
        WWISE
        #
        """
        self.wwise: WAAPI | None = None
        self.init_wwise()

    ###############################
    # UIMainWindow CLASS METHODS
    ###############################

    @Slot(QApplication)
    def update_theme(self, app: QApplication) -> None:
        if self.radioButton_theme_ose.isChecked():
            theme.set_ose_theme(app)
        if self.radioButton_theme_default.isChecked():
            theme.set_default_theme(app)

    @Slot(QApplication)
    def update_app_stay_open(self, app: QApplication) -> None:
        value = not self.checkBox_keep_app_open.isChecked()
        if value:
            app.setQuitOnLastWindowClosed(value)
            return
        app.setQuitOnLastWindowClosed(value)
        self.tray.showMessage(Info.PROJECT_TITLE,
                              f'{Info.PROJECT_TITLE} will stay open in the system tray when the window closes.',
                              QIcon(Info.ICON_PATH),
                              Info.NOTIFICATION_TIME)

    @staticmethod
    def open_documentation_link():
        webbrowser.open(Info.DOCS_LINK)

    def notify_app_open_in_tray(self):
        self.tray.showMessage(Info.PROJECT_TITLE,
                              f'{Info.PROJECT_TITLE} still open in system tray',
                              QIcon(Info.ICON_PATH),
                              Info.NOTIFICATION_TIME)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if self.checkBox_keep_app_open.isChecked():
            self.notify_app_open_in_tray()
        self.save_prefs()

    def show_splash_screen(self):
        self.splash = SplashScreen()

    def init_wwise(self) -> None:
        """
        Attempt to initialize the wwise object upon successful connection
        :return:
        """
        try:
            self.wwise = None
            self.wwise = WAAPI()
            self.update_wwise_project_info()
        except CannotConnectToWaapiException:
            self.wwise_status.setText('NO WWISE PROJECT OPEN')

    def update_wwise_project_info(self) -> None:
        """
        Update the UI to reflect the connection
        :return:
        """
        if self.is_wwise_connected():
            result: str = self.wwise.get_project_info()['name']
            self.wwise_status.setText(f'Connected to project {result.title()}')
            self.wwise_status.setToolTip('Connected')
        else:
            self.wwise_status.setText('NO WWISE PROJECT OPEN')
            self.wwise_status.setToolTip('Please open a Wwise project first')

    def is_wwise_connected(self) -> bool:
        try:
            return self.wwise.is_connected()
        except Exception as e:
            print(e)
            return False

    def select_unreal_wwise_ak_events_path(self):
        result = QFileDialog.getExistingDirectory(self, 'Select AK Events path in your Unreal Engine project')
        if result:
            self.lineEdit_ak_events_folder_in_ue.setText(result)
            self.lineEdit_ak_events_folder_in_ue.setToolTip(result)

    def get_all_wwise_ak_events(self) -> list[str]:
        if not self.wwise.is_connected():
            return []
        ak_events: list[dict] = self.wwise.get_all_event_objects()
        return [item.get('name') for item in ak_events]

    def get_all_wwise_ak_busses(self) -> list[str]:
        if not self.wwise.is_connected():
            return []
        ak_events: list[dict] = self.wwise.get_all_bus_objects()
        return [item.get('name') for item in ak_events]

    def get_all_wwise_ak_aux_busses(self) -> list[str]:
        if not self.wwise.is_connected():
            return []
        ak_events: list[dict] = self.wwise.get_all_aux_bus_objects()
        return [item.get('name') for item in ak_events]

    def add_selection_to_exclusions_list(self):
        selected_items: list[QListWidgetItem] = self.listWidget_ak_events.selectedItems()
        if selected_items:
            self.ak_event_exclusions = [item.text() for item in selected_items]
            self.listWidget_exclusions.addItems(self.ak_event_exclusions)

    def get_all_ue_ak_events(self, file_path_to_ak_events: str) -> list[str]:
        path: Path = Path(file_path_to_ak_events)
        if not path.exists():
            self.display_invalid_folder_dialog(file_path_to_ak_events)
            return []
        return [Path(file).stem for file in glob.glob(str(path / '**' / '*.uasset'), recursive=True)]

    def display_invalid_folder_dialog(self, folder: str):
        dialog = QDialog(self, Qt.WindowType.Dialog)
        dialog.setWindowTitle(f'Folder not found')
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'It appears folder {folder} doesn\'t exist'))
        dialog.setLayout(layout)
        dialog.show()

    def diff_ue_ak_events_folder_against_wwise_events(self):
        self.listWidget_ak_events.clear()
        self.ak_events_to_delete.clear()
        wwise_proj_ak_objects: list[str] = []
        match self.comboBox_diff_type.currentText():
            case "events":
                wwise_proj_ak_objects: list[str] = self.get_all_wwise_ak_events()
            case 'busses':
                wwise_proj_ak_objects: list[str] = self.get_all_wwise_ak_busses()
            case 'aux busses':
                wwise_proj_ak_objects: list[str] = self.get_all_wwise_ak_aux_busses()

        ue_proj_ak_assets: list[str] = self.get_all_ue_ak_events(self.lineEdit_ak_events_folder_in_ue.text())
        self.label_num_events_in_wwise_project.setText(str(len(wwise_proj_ak_objects)))
        self.label_num_events_in_ue_project.setText(str(len(ue_proj_ak_assets)))
        self.add_list_widget_items(ue_proj_ak_assets, wwise_proj_ak_objects)
        self.label_number_of_events_to_delete.setText(str(len(self.ak_events_to_delete)))

    def add_list_widget_items(self, ue_proj_ak_assets: list[str], wwise_proj_ak_objects: list[str]):
        for event in wwise_proj_ak_objects:
            item: QListWidgetItem = QListWidgetItem(event)
            if event not in ue_proj_ak_assets and event not in self.ak_event_exclusions:
                item.setBackground(QtGui.QColor(150, 0, 0))
                self.ak_events_to_delete.append(event)
                self.listWidget_ak_events.addItem(item)
            if not self.checkBox_only_show_invalid.isChecked():
                self.listWidget_ak_events.addItem(item)

    def confirm_delete_unused_ak_events(self) -> None:
        if not self.wwise.is_connected():
            return
        self.confirm: QDialog = QDialog(self, Qt.WindowType.Dialog)
        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(QLabel('Delete unused AK events?\nPlease be sure that you\'ve '
                                'reconciled all ak events in Unreal.\nFailing to do so could cause some events '
                                'to break the build, since there\'s a chance that the .uasset has a different name '
                                'than the name used in Wwise.'))
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.confirm.buttonBox = QDialogButtonBox(buttons)
        self.confirm.buttonBox.accepted.connect(self.delete_unused_ak_events)
        self.confirm.buttonBox.rejected.connect(self.confirm.close)
        layout.addWidget(self.confirm.buttonBox)
        self.confirm.setLayout(layout)
        self.confirm.show()

    def delete_unused_ak_events(self) -> None:
        self.confirm.close()
        for event in self.ak_events_to_delete:
            print(f'Deleted: {event}')
            self.wwise.delete_event(self.wwise.get_event_guid_from_name(event))

    def copy_list_to_clipboard(self):
        list_items: list[str] = [self.listWidget_ak_events.item(index).text()
                                 for index in
                                 self.listWidget_ak_events.count()
                                 ]
        pyperclip.copy('\n'.join(list_items))

    @staticmethod
    def get_parse_wav_import_file(paths: list) -> list:
        return [str(Path(path).parent).split('\\') for path in paths]

    def convert_widgets_to_prefs_dict(self) -> dict:
        prefs = {}
        for obj in self.PREFERENCES_OBJECTS:
            obj_dict = self.get_widget_dict_from_value(obj)
            print(obj_dict)
            if obj_dict:
                prefs.update(obj_dict)
        return prefs

    def update_progress_state(self):
        """Update UI elements to reflect current progress state"""
        self.tray.showMessage("Updating....")
        if self.wwise and self.wwise.is_connected():
            if self.progress_window:
                self.progress_window.label_progress_item.setText("Updating progress")

    def get_widget_dict_from_value(self, obj) -> dict:
        name: str = self.get_object_type_name(obj)
        obj_class = obj.__class__
        value: any = self.update_matched_qt_widgets(obj, obj_class)

        if value is not None:
            return {name: {'value': value, 'type': str(obj_class)}}
        return {}

    def update_matched_qt_widgets(self, obj: any, obj_class: any, value_to_set: any = None, edit: bool = False) -> any:
        value = None
        match obj_class:
            case QtWidgets.QCheckBox:
                value = UIMainWindow._update_q_checkbox(edit, obj, value_to_set)
            case QtWidgets.QLineEdit:
                value = UIMainWindow._update_q_line_edit(edit, obj, value_to_set)
            case QtWidgets.QTextEdit:
                value = UIMainWindow._update_q_text_edit(edit, obj, value_to_set)
            case QtWidgets.QRadioButton:
                value = UIMainWindow._update_q_radio_button(edit, obj, value_to_set)
            case QtWidgets.QTreeWidget:
                value = self._update_q_tree_widget(edit, obj, value_to_set)
            case QtWidgets.QStackedWidget:
                value = UIMainWindow._update_q_stacked_widget(edit, obj, value_to_set)
            case QtWidgets.QGroupBox:
                value = UIMainWindow._update_q_groupbox_widget(edit, obj, value_to_set)
            case builtins.list:
                value = UIMainWindow._update_list_of_strings(edit, obj, value_to_set)
            case _:
                pass
        return value

    @staticmethod
    def _update_q_checkbox(edit, obj, value_to_set) -> bool | None:
        if edit and value_to_set is not None:
            obj.setChecked(value_to_set)
        else:
            return obj.isChecked()

    @staticmethod
    def _update_q_line_edit(edit, obj, value_to_set) -> str | None:
        if edit and value_to_set is not None:
            obj.setText(value_to_set)
        else:
            return obj.text()

    @staticmethod
    def _update_q_text_edit(edit, obj, value_to_set) -> str | None:
        if edit and value_to_set is not None:
            obj.setText(value_to_set)
        else:
            return obj.text()

    @staticmethod
    def _update_q_radio_button(edit, obj, value_to_set) -> bool | None:
        if edit and value_to_set is not None:
            obj.setChecked(value_to_set)
        else:
            return obj.isChecked()

    def _update_q_tree_widget(
            self,
            edit: bool,
            obj: QTreeWidget,
            value_to_set: list[list[str]]
    ) -> list[list[str]] | None:
        if edit and value_to_set is not None:
            for row in value_to_set:
                item = QTreeWidgetItem(row)
                item.setFlags(self.QT_WIDGET_TREE_ITEM_FLAGS)
                obj.addTopLevelItem(item)
        else:
            return UIMainWindow.get_q_treewidget_as_list(obj)

    @staticmethod
    def get_q_treewidget_as_list(obj: QTreeWidget) -> list[list[str]]:
        return [
            [
                obj.topLevelItem(i).data(j, 0)
                for j in range(obj.columnCount())
            ]
            for i in range(obj.topLevelItemCount())
        ]

    @staticmethod
    def _update_q_stacked_widget(edit: bool, obj: QStackedWidget, value_to_set: int) -> int | None:
        if edit and value_to_set is not None:
            obj.setCurrentIndex(value_to_set)
        else:
            return obj.currentIndex()

    @staticmethod
    def _update_q_groupbox_widget(edit: bool, obj: QGroupBox, value_to_set: bool) -> bool | None:
        if edit and value_to_set is not None:
            obj.setChecked(value_to_set)
        else:
            return obj.isChecked()

    @staticmethod
    def _update_list_of_strings(edit: bool, obj: list[str], value_to_set: list[str]) -> list | None:
        if edit and value_to_set is not None:
            obj.clear()
            obj.extend(value_to_set)
        else:
            return obj

    def save_prefs(self) -> None:
        print('Saving preferences')
        ProjectFile.save(self.convert_widgets_to_prefs_dict(), self.PREFERENCES_FILE)

    def load_prefs(self) -> None:
        print('Loading preferences')
        prefs: dict = ProjectFile.load(self.PREFERENCES_FILE)
        if prefs:
            if not prefs['checkBox_use_persistent_data']['value']:
                self.checkBox_use_persistent_data.setChecked(False)
                return
            for obj in self.PREFERENCES_OBJECTS:
                name: str = self.get_object_type_name(obj)
                if isinstance(prefs, dict) and name in prefs.keys():
                    self.update_matched_qt_widgets(
                        obj,
                        obj.__class__,
                        value_to_set=prefs[name]['value'],
                        edit=True
                    )

    @staticmethod
    def get_object_type_name(obj) -> str:
        name: str = ''
        if isinstance(obj, QObject):
            name = obj.objectName()
        else:
            for name, value in locals().items():
                if value is obj:
                    return name
        return name

    def open_preferences(self) -> None:
        self.stackedWidget.setCurrentIndex(0)

    def open_main_page(self) -> None:
        self.stackedWidget.setCurrentIndex(1)

    def open_second_page(self) -> None:
        self.stackedWidget.setCurrentIndex(2)

    @staticmethod
    def get_prefs_path() -> str:
        file = f'{Info.PROJECT_TITLE.lower()}{FileTypes.PREFS}'
        parent_path = Path().joinpath(Path().home(), Info.PROJECT_TITLE)
        parent_path.mkdir(exist_ok=True)
        parent_path = str(parent_path.joinpath(file))
        print('Preferences Path: ', parent_path)
        return parent_path

    @Slot()
    def hide_progress_bar(self) -> None:
        self.continue_importing = False
        self.progress_window.close()

    @Slot()
    def show_progress_bar(self) -> None:
        self.continue_importing = True
        self.progress_window = ProgressBarWindow(self)
        self.progress_window.setWindowTitle(f'{Info.PROJECT_TITLE} | Importing')
        self.progress_window.show()
        self.progress_window.raise_()
        self.progress_window.buttonBox.rejected.connect(self.hide_progress_bar)

    @Slot(str)
    def update_progress_bar_message(self, message: str) -> None:
        if self.progress_window:
            self.progress_window.label_progress_item.setText(message)

    @Slot(int)
    def update_progress_bar_value(self, value: int) -> None:
        if self.progress_window:
            self.progress_window.progressBar_import_progress.setValue(value)

    @Slot(int)
    def update_progress_bar_maximum(self, value: int) -> None:
        if self.progress_window:
            self.progress_window.progressBar_import_progress.setMaximum(value)
