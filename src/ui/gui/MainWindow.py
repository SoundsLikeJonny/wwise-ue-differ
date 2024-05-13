# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 899)
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSee_documentation = QAction(MainWindow)
        self.actionSee_documentation.setObjectName(u"actionSee_documentation")
        self.actionMain_Window = QAction(MainWindow)
        self.actionMain_Window.setObjectName(u"actionMain_Window")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionOverrides = QAction(MainWindow)
        self.actionOverrides.setObjectName(u"actionOverrides")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionRefresh_table = QAction(MainWindow)
        self.actionRefresh_table.setObjectName(u"actionRefresh_table")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_preferences = QWidget()
        self.page_preferences.setObjectName(u"page_preferences")
        self.gridLayout_4 = QGridLayout(self.page_preferences)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_to_main_page = QPushButton(self.page_preferences)
        self.pushButton_to_main_page.setObjectName(u"pushButton_to_main_page")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_to_main_page.sizePolicy().hasHeightForWidth())
        self.pushButton_to_main_page.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.pushButton_to_main_page, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.checkBox_keep_app_open = QCheckBox(self.page_preferences)
        self.checkBox_keep_app_open.setObjectName(u"checkBox_keep_app_open")

        self.gridLayout_4.addWidget(self.checkBox_keep_app_open, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.checkBox_use_persistent_data = QCheckBox(self.page_preferences)
        self.checkBox_use_persistent_data.setObjectName(u"checkBox_use_persistent_data")
        self.checkBox_use_persistent_data.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_use_persistent_data, 3, 0, 1, 1)

        self.groupBox = QGroupBox(self.page_preferences)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton_theme_default = QRadioButton(self.groupBox)
        self.radioButton_theme_default.setObjectName(u"radioButton_theme_default")
        self.radioButton_theme_default.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_theme_default, 0, 0, 1, 1)

        self.radioButton_theme_ose = QRadioButton(self.groupBox)
        self.radioButton_theme_ose.setObjectName(u"radioButton_theme_ose")

        self.gridLayout.addWidget(self.radioButton_theme_ose, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_preferences)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.gridLayout_3 = QGridLayout(self.page_main)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 4, 6, 1, 1)

        self.line = QFrame(self.page_main)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 1, 1, 10)

        self.comboBox_languages = QComboBox(self.page_main)
        self.comboBox_languages.setObjectName(u"comboBox_languages")

        self.gridLayout_3.addWidget(self.comboBox_languages, 4, 5, 1, 1)

        self.checkBox_is_streaming = QCheckBox(self.page_main)
        self.checkBox_is_streaming.setObjectName(u"checkBox_is_streaming")
        self.checkBox_is_streaming.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_is_streaming, 4, 9, 1, 1)

        self.checkBox_clear_on_csv_loading = QCheckBox(self.page_main)
        self.checkBox_clear_on_csv_loading.setObjectName(u"checkBox_clear_on_csv_loading")
        self.checkBox_clear_on_csv_loading.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_clear_on_csv_loading, 6, 4, 1, 2)

        self.label_5 = QLabel(self.page_main)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.label_5, 4, 4, 1, 1)

        self.pushButton_refresh = QPushButton(self.page_main)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.gridLayout_3.addWidget(self.pushButton_refresh, 6, 10, 1, 1)

        self.pushButton_clear_tree = QPushButton(self.page_main)
        self.pushButton_clear_tree.setObjectName(u"pushButton_clear_tree")

        self.gridLayout_3.addWidget(self.pushButton_clear_tree, 6, 3, 1, 1)

        self.pushButton_remove_selected_tree_widget_rows = QPushButton(self.page_main)
        self.pushButton_remove_selected_tree_widget_rows.setObjectName(u"pushButton_remove_selected_tree_widget_rows")
        sizePolicy.setHeightForWidth(self.pushButton_remove_selected_tree_widget_rows.sizePolicy().hasHeightForWidth())
        self.pushButton_remove_selected_tree_widget_rows.setSizePolicy(sizePolicy)
        self.pushButton_remove_selected_tree_widget_rows.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_remove_selected_tree_widget_rows, 6, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.page_main)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_import_errors = QLabel(self.page_main)
        self.label_import_errors.setObjectName(u"label_import_errors")

        self.horizontalLayout_3.addWidget(self.label_import_errors)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 6, 8, 1, 1)

        self.checkBox_generate_soundbanks = QCheckBox(self.page_main)
        self.checkBox_generate_soundbanks.setObjectName(u"checkBox_generate_soundbanks")

        self.gridLayout_3.addWidget(self.checkBox_generate_soundbanks, 4, 8, 1, 1)

        self.treeWidget_wwise_info = QTreeWidget(self.page_main)
        QTreeWidgetItem(self.treeWidget_wwise_info)
        self.treeWidget_wwise_info.setObjectName(u"treeWidget_wwise_info")
        self.treeWidget_wwise_info.setEnabled(True)
        self.treeWidget_wwise_info.setAutoFillBackground(False)
        self.treeWidget_wwise_info.setFrameShadow(QFrame.Plain)
        self.treeWidget_wwise_info.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.treeWidget_wwise_info.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.treeWidget_wwise_info, 5, 1, 1, 10)

        self.pushButton_import = QPushButton(self.page_main)
        self.pushButton_import.setObjectName(u"pushButton_import")

        self.gridLayout_3.addWidget(self.pushButton_import, 4, 10, 1, 1)

        self.checkBox_use_overrides = QCheckBox(self.page_main)
        self.checkBox_use_overrides.setObjectName(u"checkBox_use_overrides")

        self.gridLayout_3.addWidget(self.checkBox_use_overrides, 4, 7, 1, 1)

        self.pushButton_load_csv = QPushButton(self.page_main)
        self.pushButton_load_csv.setObjectName(u"pushButton_load_csv")
        self.pushButton_load_csv.setEnabled(True)

        self.gridLayout_3.addWidget(self.pushButton_load_csv, 4, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.wwise_status_refresh = QPushButton(self.page_main)
        self.wwise_status_refresh.setObjectName(u"wwise_status_refresh")

        self.horizontalLayout.addWidget(self.wwise_status_refresh)

        self.label = QLabel(self.page_main)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.wwise_status = QLabel(self.page_main)
        self.wwise_status.setObjectName(u"wwise_status")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(4)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.wwise_status.sizePolicy().hasHeightForWidth())
        self.wwise_status.setSizePolicy(sizePolicy2)
        self.wwise_status.setMinimumSize(QSize(172, 0))
        self.wwise_status.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.wwise_status)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.pushButton_main_page_to_overrides = QPushButton(self.page_main)
        self.pushButton_main_page_to_overrides.setObjectName(u"pushButton_main_page_to_overrides")

        self.horizontalLayout.addWidget(self.pushButton_main_page_to_overrides)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 10)

        self.stackedWidget.addWidget(self.page_main)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_30 = QLabel(self.page)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)

        self.gridLayout_5.addWidget(self.label_30, 2, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_actor_mixer = QGroupBox(self.widget_2)
        self.groupBox_actor_mixer.setObjectName(u"groupBox_actor_mixer")
        self.groupBox_actor_mixer.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_actor_mixer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.groupBox_actor_mixer)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_13 = QLabel(self.groupBox_actor_mixer)
        self.label_13.setObjectName(u"label_13")
        font1 = QFont()
        font1.setBold(False)
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_19 = QLabel(self.groupBox_actor_mixer)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_2.addWidget(self.label_19)

        self.label_20 = QLabel(self.groupBox_actor_mixer)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_20)

        self.groupBox_override_actormixer_parent = QGroupBox(self.groupBox_actor_mixer)
        self.groupBox_override_actormixer_parent.setObjectName(u"groupBox_override_actormixer_parent")
        self.groupBox_override_actormixer_parent.setFlat(True)
        self.groupBox_override_actormixer_parent.setCheckable(True)
        self.groupBox_override_actormixer_parent.setChecked(True)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_override_actormixer_parent)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_override_actormixer_parent = QLineEdit(self.groupBox_override_actormixer_parent)
        self.lineEdit_override_actormixer_parent.setObjectName(u"lineEdit_override_actormixer_parent")
        self.lineEdit_override_actormixer_parent.setEnabled(True)
        self.lineEdit_override_actormixer_parent.setClearButtonEnabled(False)

        self.verticalLayout_6.addWidget(self.lineEdit_override_actormixer_parent)


        self.verticalLayout_2.addWidget(self.groupBox_override_actormixer_parent)

        self.label_29 = QLabel(self.groupBox_actor_mixer)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_29)

        self.groupBox_override_actormixer_mission = QGroupBox(self.groupBox_actor_mixer)
        self.groupBox_override_actormixer_mission.setObjectName(u"groupBox_override_actormixer_mission")
        self.groupBox_override_actormixer_mission.setFlat(True)
        self.groupBox_override_actormixer_mission.setCheckable(True)
        self.groupBox_override_actormixer_mission.setChecked(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_override_actormixer_mission)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit_override_actormixer_mission = QLineEdit(self.groupBox_override_actormixer_mission)
        self.lineEdit_override_actormixer_mission.setObjectName(u"lineEdit_override_actormixer_mission")

        self.verticalLayout_7.addWidget(self.lineEdit_override_actormixer_mission)


        self.verticalLayout_2.addWidget(self.groupBox_override_actormixer_mission)

        self.label_28 = QLabel(self.groupBox_actor_mixer)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_28)

        self.groupBox_override_actormixer_persona = QGroupBox(self.groupBox_actor_mixer)
        self.groupBox_override_actormixer_persona.setObjectName(u"groupBox_override_actormixer_persona")
        self.groupBox_override_actormixer_persona.setFlat(True)
        self.groupBox_override_actormixer_persona.setCheckable(True)
        self.groupBox_override_actormixer_persona.setChecked(False)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_override_actormixer_persona)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lineEdit_override_actormixer_persona = QLineEdit(self.groupBox_override_actormixer_persona)
        self.lineEdit_override_actormixer_persona.setObjectName(u"lineEdit_override_actormixer_persona")

        self.verticalLayout_8.addWidget(self.lineEdit_override_actormixer_persona)


        self.verticalLayout_2.addWidget(self.groupBox_override_actormixer_persona)

        self.label_27 = QLabel(self.groupBox_actor_mixer)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_27)

        self.label_2 = QLabel(self.groupBox_actor_mixer)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.groupBox_actor_mixer)

        self.groupBox_events = QGroupBox(self.widget_2)
        self.groupBox_events.setObjectName(u"groupBox_events")
        self.groupBox_events.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_events)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.groupBox_events)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)

        self.label_16 = QLabel(self.groupBox_events)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_16)

        self.groupBox_override_eventfolder_parent = QGroupBox(self.groupBox_events)
        self.groupBox_override_eventfolder_parent.setObjectName(u"groupBox_override_eventfolder_parent")
        self.groupBox_override_eventfolder_parent.setFlat(True)
        self.groupBox_override_eventfolder_parent.setCheckable(True)
        self.groupBox_override_eventfolder_parent.setChecked(True)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_override_eventfolder_parent)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_override_eventfolder_parent = QLineEdit(self.groupBox_override_eventfolder_parent)
        self.lineEdit_override_eventfolder_parent.setObjectName(u"lineEdit_override_eventfolder_parent")

        self.verticalLayout_9.addWidget(self.lineEdit_override_eventfolder_parent)


        self.verticalLayout_4.addWidget(self.groupBox_override_eventfolder_parent)

        self.label_23 = QLabel(self.groupBox_events)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_23)

        self.groupBox_override_eventfolder_mission = QGroupBox(self.groupBox_events)
        self.groupBox_override_eventfolder_mission.setObjectName(u"groupBox_override_eventfolder_mission")
        self.groupBox_override_eventfolder_mission.setFlat(True)
        self.groupBox_override_eventfolder_mission.setCheckable(True)
        self.groupBox_override_eventfolder_mission.setChecked(False)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_override_eventfolder_mission)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lineEdit_override_eventfolder_mission = QLineEdit(self.groupBox_override_eventfolder_mission)
        self.lineEdit_override_eventfolder_mission.setObjectName(u"lineEdit_override_eventfolder_mission")

        self.verticalLayout_10.addWidget(self.lineEdit_override_eventfolder_mission)


        self.verticalLayout_4.addWidget(self.groupBox_override_eventfolder_mission)

        self.label_22 = QLabel(self.groupBox_events)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_22)

        self.label_3 = QLabel(self.groupBox_events)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.groupBox_events)

        self.groupBox_soundbanks = QGroupBox(self.widget_2)
        self.groupBox_soundbanks.setObjectName(u"groupBox_soundbanks")
        self.groupBox_soundbanks.setCheckable(False)
        self.groupBox_soundbanks.setChecked(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_soundbanks)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_12 = QLabel(self.groupBox_soundbanks)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_5.addWidget(self.label_12)

        self.label_18 = QLabel(self.groupBox_soundbanks)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_18)

        self.groupBox_override_soundbankfolder_parent = QGroupBox(self.groupBox_soundbanks)
        self.groupBox_override_soundbankfolder_parent.setObjectName(u"groupBox_override_soundbankfolder_parent")
        self.groupBox_override_soundbankfolder_parent.setFlat(True)
        self.groupBox_override_soundbankfolder_parent.setCheckable(True)
        self.groupBox_override_soundbankfolder_parent.setChecked(True)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_override_soundbankfolder_parent)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lineEdit_override_soundbankfolder_parent = QLineEdit(self.groupBox_override_soundbankfolder_parent)
        self.lineEdit_override_soundbankfolder_parent.setObjectName(u"lineEdit_override_soundbankfolder_parent")

        self.verticalLayout_11.addWidget(self.lineEdit_override_soundbankfolder_parent)


        self.verticalLayout_5.addWidget(self.groupBox_override_soundbankfolder_parent)

        self.label_25 = QLabel(self.groupBox_soundbanks)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_25)

        self.groupBox_override_soundbankfolder_mission = QGroupBox(self.groupBox_soundbanks)
        self.groupBox_override_soundbankfolder_mission.setObjectName(u"groupBox_override_soundbankfolder_mission")
        self.groupBox_override_soundbankfolder_mission.setFlat(True)
        self.groupBox_override_soundbankfolder_mission.setCheckable(True)
        self.groupBox_override_soundbankfolder_mission.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_override_soundbankfolder_mission)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lineEdit_override_soundbankfolder_mission = QLineEdit(self.groupBox_override_soundbankfolder_mission)
        self.lineEdit_override_soundbankfolder_mission.setObjectName(u"lineEdit_override_soundbankfolder_mission")

        self.verticalLayout_12.addWidget(self.lineEdit_override_soundbankfolder_mission)


        self.verticalLayout_5.addWidget(self.groupBox_override_soundbankfolder_mission)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.horizontalLayout_2.addWidget(self.groupBox_soundbanks)


        self.gridLayout_5.addWidget(self.widget_2, 3, 0, 1, 2)

        self.pushButton_overrides_to_main_page = QPushButton(self.page)
        self.pushButton_overrides_to_main_page.setObjectName(u"pushButton_overrides_to_main_page")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_overrides_to_main_page.sizePolicy().hasHeightForWidth())
        self.pushButton_overrides_to_main_page.setSizePolicy(sizePolicy3)

        self.gridLayout_5.addWidget(self.pushButton_overrides_to_main_page, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.page)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 947, 21))
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuInfo.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuInfo.addAction(self.actionInfo)
        self.menuInfo.addSeparator()
        self.menuInfo.addAction(self.actionSave)
        self.menuInfo.addSeparator()
        self.menuInfo.addAction(self.actionPreferences)
        self.menuInfo.addSeparator()
        self.menuInfo.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionSee_documentation)
        self.menuView.addAction(self.actionMain_Window)
        self.menuView.addAction(self.actionOverrides)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionRefresh_table)

        self.retranslateUi(MainWindow)
        self.pushButton_clear_tree.pressed.connect(self.treeWidget_wwise_info.clear)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dialogue Importer", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
#if QT_CONFIG(shortcut)
        self.actionInfo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+0", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSee_documentation.setText(QCoreApplication.translate("MainWindow", u"See docs in Confluence", None))
#if QT_CONFIG(tooltip)
        self.actionSee_documentation.setToolTip(QCoreApplication.translate("MainWindow", u"See docs in Confluence", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSee_documentation.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionMain_Window.setText(QCoreApplication.translate("MainWindow", u"Main Window", None))
#if QT_CONFIG(shortcut)
        self.actionMain_Window.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
#if QT_CONFIG(shortcut)
        self.actionPreferences.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actionOverrides.setText(QCoreApplication.translate("MainWindow", u"Overrides", None))
#if QT_CONFIG(shortcut)
        self.actionOverrides.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionRefresh_table.setText(QCoreApplication.translate("MainWindow", u"Refresh Table", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh_table.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_to_main_page.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.checkBox_keep_app_open.setText(QCoreApplication.translate("MainWindow", u"Stay open in system tray on close", None))
        self.checkBox_use_persistent_data.setText(QCoreApplication.translate("MainWindow", u"Load persistent data between uses (includes settings)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"UI Theme", None))
        self.radioButton_theme_default.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.radioButton_theme_ose.setText(QCoreApplication.translate("MainWindow", u"ose (Dark grey w/ yellow)", None))
        self.checkBox_is_streaming.setText(QCoreApplication.translate("MainWindow", u"Stream", None))
        self.checkBox_clear_on_csv_loading.setText(QCoreApplication.translate("MainWindow", u"Clear table before loading CSVs", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Language: ", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton_clear_tree.setText(QCoreApplication.translate("MainWindow", u"Clear Table", None))
        self.pushButton_remove_selected_tree_widget_rows.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.label_8.setText("")
        self.label_import_errors.setText("")
        self.checkBox_generate_soundbanks.setText(QCoreApplication.translate("MainWindow", u"Create Soundbanks", None))
        ___qtreewidgetitem = self.treeWidget_wwise_info.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Persona", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"SubPath", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"ParentPath", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u".wav", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));

        __sortingEnabled = self.treeWidget_wwise_info.isSortingEnabled()
        self.treeWidget_wwise_info.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_wwise_info.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"test", None));
        self.treeWidget_wwise_info.setSortingEnabled(__sortingEnabled)

        self.pushButton_import.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.checkBox_use_overrides.setText(QCoreApplication.translate("MainWindow", u"Use overrides", None))
        self.pushButton_load_csv.setText(QCoreApplication.translate("MainWindow", u"Load CSV Files", None))
        self.wwise_status_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wwise Status: ", None))
        self.wwise_status.setText(QCoreApplication.translate("MainWindow", u"NO WWISE PROJECT OPEN", None))
        self.pushButton_main_page_to_overrides.setText(QCoreApplication.translate("MainWindow", u"Overrides ->", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Overrides", None))
        self.groupBox_actor_mixer.setTitle(QCoreApplication.translate("MainWindow", u"Actor-Mixers", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dialogue WorkUnit", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Dialogue Actor-Mixer", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.groupBox_override_actormixer_parent.setTitle(QCoreApplication.translate("MainWindow", u"Override Parent Actor-Mixer", None))
        self.lineEdit_override_actormixer_parent.setText(QCoreApplication.translate("MainWindow", u"TEST", None))
        self.lineEdit_override_actormixer_parent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mission", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.groupBox_override_actormixer_mission.setTitle(QCoreApplication.translate("MainWindow", u"Override Mission Actor-Mixer", None))
        self.lineEdit_override_actormixer_mission.setText("")
        self.lineEdit_override_actormixer_mission.setPlaceholderText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.groupBox_override_actormixer_persona.setTitle(QCoreApplication.translate("MainWindow", u"Override Persona Actor-Mixer", None))
        self.lineEdit_override_actormixer_persona.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ryana", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"[Name] Sound Voice", None))
        self.groupBox_events.setTitle(QCoreApplication.translate("MainWindow", u"Events", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dialogue WorkUnit", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.groupBox_override_eventfolder_parent.setTitle(QCoreApplication.translate("MainWindow", u"Override Parent Folder", None))
        self.lineEdit_override_eventfolder_parent.setText(QCoreApplication.translate("MainWindow", u"TEST", None))
        self.lineEdit_override_eventfolder_parent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mission", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.groupBox_override_eventfolder_mission.setTitle(QCoreApplication.translate("MainWindow", u"Override Mission Folder", None))
        self.lineEdit_override_eventfolder_mission.setPlaceholderText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"[Name] Event", None))
        self.groupBox_soundbanks.setTitle(QCoreApplication.translate("MainWindow", u"SoundBanks", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"SoundBanks WorkUnit", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.groupBox_override_soundbankfolder_parent.setTitle(QCoreApplication.translate("MainWindow", u"Override Parent Folder", None))
        self.lineEdit_override_soundbankfolder_parent.setText(QCoreApplication.translate("MainWindow", u"TEST", None))
        self.lineEdit_override_soundbankfolder_parent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mission", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.groupBox_override_soundbankfolder_mission.setTitle(QCoreApplication.translate("MainWindow", u"Override Mission Soundbank", None))
        self.lineEdit_override_soundbankfolder_mission.setPlaceholderText("")
        self.pushButton_overrides_to_main_page.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

