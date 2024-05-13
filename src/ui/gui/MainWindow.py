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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 843)
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
        self.pushButton_remove_selected_tree_widget_rows = QPushButton(self.page_main)
        self.pushButton_remove_selected_tree_widget_rows.setObjectName(u"pushButton_remove_selected_tree_widget_rows")
        self.pushButton_remove_selected_tree_widget_rows.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_remove_selected_tree_widget_rows.sizePolicy().hasHeightForWidth())
        self.pushButton_remove_selected_tree_widget_rows.setSizePolicy(sizePolicy)
        self.pushButton_remove_selected_tree_widget_rows.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_remove_selected_tree_widget_rows, 7, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 4, 1, 1)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wwise_status.sizePolicy().hasHeightForWidth())
        self.wwise_status.setSizePolicy(sizePolicy1)
        self.wwise_status.setMinimumSize(QSize(172, 0))
        self.wwise_status.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.wwise_status)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 6)

        self.label_2 = QLabel(self.page_main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1)

        self.line = QFrame(self.page_main)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 1, 1, 6)

        self.pushButton_clear_tree = QPushButton(self.page_main)
        self.pushButton_clear_tree.setObjectName(u"pushButton_clear_tree")
        self.pushButton_clear_tree.setEnabled(False)

        self.gridLayout_3.addWidget(self.pushButton_clear_tree, 7, 2, 1, 1)

        self.pushButton_refresh = QPushButton(self.page_main)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setEnabled(False)

        self.gridLayout_3.addWidget(self.pushButton_refresh, 7, 6, 1, 1)

        self.pushButton = QPushButton(self.page_main)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.pushButton, 2, 6, 1, 1)

        self.treeWidget_wwise_info = QTreeWidget(self.page_main)
        self.treeWidget_wwise_info.setObjectName(u"treeWidget_wwise_info")
        self.treeWidget_wwise_info.setEnabled(True)
        self.treeWidget_wwise_info.setAutoFillBackground(False)
        self.treeWidget_wwise_info.setFrameShadow(QFrame.Plain)
        self.treeWidget_wwise_info.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.treeWidget_wwise_info.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.treeWidget_wwise_info, 5, 1, 1, 6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 6, 2, 1, 1)

        self.lineEdit_ak_events_folder_in_ue = QLineEdit(self.page_main)
        self.lineEdit_ak_events_folder_in_ue.setObjectName(u"lineEdit_ak_events_folder_in_ue")

        self.gridLayout_3.addWidget(self.lineEdit_ak_events_folder_in_ue, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 7, 5, 1, 1)

        self.pushButton_browse_select_ak_event_folder = QPushButton(self.page_main)
        self.pushButton_browse_select_ak_event_folder.setObjectName(u"pushButton_browse_select_ak_event_folder")

        self.gridLayout_3.addWidget(self.pushButton_browse_select_ak_event_folder, 2, 3, 1, 1)

        self.stackedWidget.addWidget(self.page_main)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget.addWidget(self.page)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)


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
        self.radioButton_theme_ose.setText(QCoreApplication.translate("MainWindow", u"OSE (Dark grey w/ Cyan)", None))
        self.pushButton_remove_selected_tree_widget_rows.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.wwise_status_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh Connection", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"WAAPI Status: ", None))
        self.wwise_status.setText(QCoreApplication.translate("MainWindow", u"NO WWISE PROJECT OPEN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"AkEvents Folder In Unreal Engine", None))
        self.pushButton_clear_tree.setText(QCoreApplication.translate("MainWindow", u"Clear Table", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Populate the table with info", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Diff Against UE Folder", None))
#if QT_CONFIG(tooltip)
        self.pushButton_browse_select_ak_event_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Select the Ak Events folder in your Unreal Engine project", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_browse_select_ak_event_folder.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

