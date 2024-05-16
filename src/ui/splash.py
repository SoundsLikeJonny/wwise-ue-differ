from pathlib import Path

from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import (
    Qt,
    QTimer,
    QCoreApplication, Signal
)
from PySide6.QtGui import (
    QFont,
    QPixmap,
    QColor, QMouseEvent,

)
from PySide6.QtWidgets import (
    QLabel,
    QSplashScreen,
    QVBoxLayout,
    QWidget, QDialog, QMainWindow,
)
from project_info import Info
import resources
from ui.gui.splash import Ui_splash_screen


class SplashScreen(QDialog, Ui_splash_screen):
    signal_splash_screen_closed = Signal()

    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.setupUi(self)
        self.splash_screen = QSplashScreen()
        self.splash_screen.setPixmap(QPixmap(':/resources/ose_splash.png'))
        self.splash_screen.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.label_footer.setText(f'{Info.COPYRIGHT}\n'
                                  f'{Info.NOTICE}')
        self.label_tool_title.setText(Info.PROJECT_TITLE)
        layout = QVBoxLayout()
        layout.addWidget(self.topLevelWidget())
        self.splash_screen.setLayout(layout)
        self.splash_screen.show()
        QCoreApplication.processEvents()
        print('New splash screen')

    def mousePressEvent(self, mouse_event: QMouseEvent) -> None:
        self.splash_screen.close()
        self.close()

    def close(self) -> None:
        super().close()
        self.signal_splash_screen_closed.emit()
