# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgressWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QProgressBar, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(713, 84)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_static_progress = QLabel(Dialog)
        self.label_static_progress.setObjectName(u"label_static_progress")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_static_progress.sizePolicy().hasHeightForWidth())
        self.label_static_progress.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_static_progress)

        self.label_progress_item = QLabel(Dialog)
        self.label_progress_item.setObjectName(u"label_progress_item")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_progress_item.sizePolicy().hasHeightForWidth())
        self.label_progress_item.setSizePolicy(sizePolicy1)
        self.label_progress_item.setMinimumSize(QSize(200, 0))
        self.label_progress_item.setFrameShadow(QFrame.Raised)
        self.label_progress_item.setTextFormat(Qt.AutoText)
        self.label_progress_item.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label_progress_item)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.progressBar_import_progress = QProgressBar(Dialog)
        self.progressBar_import_progress.setObjectName(u"progressBar_import_progress")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar_import_progress.sizePolicy().hasHeightForWidth())
        self.progressBar_import_progress.setSizePolicy(sizePolicy2)
        self.progressBar_import_progress.setMaximumSize(QSize(16777215, 10))
        self.progressBar_import_progress.setMaximum(0)
        self.progressBar_import_progress.setValue(0)
        self.progressBar_import_progress.setTextVisible(True)
        self.progressBar_import_progress.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar_import_progress)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy3)
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.horizontalLayout.addWidget(self.buttonBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_static_progress.setText(QCoreApplication.translate("Dialog", u"Import Progress:", None))
        self.label_progress_item.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.progressBar_import_progress.setFormat(QCoreApplication.translate("Dialog", u" %v/%m", None))
    # retranslateUi

