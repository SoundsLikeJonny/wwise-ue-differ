from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import (
    Qt,
    QTimer,
    QCoreApplication
)
from PySide6.QtGui import (
    QFont,
    QPixmap,
    QColor,

)
from PySide6.QtWidgets import (
    QLabel,
    QSplashScreen,
    QVBoxLayout,
    QWidget,
)
from project_info import Info
import resources


def show_splash() -> QSplashScreen:
    """
    Display general info in the pro
    :return:
    """

    data = None
    try:

        with open('info.txt') as file:
            data = file.read()
    except EOFError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)

    if data:
        pixmap = QPixmap(Info.SPLASH_PATH)
        splash = QSplashScreen(pixmap)
        # splash.setFont(QFont('Arial', 10))
        splash.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        layout = QVBoxLayout()
        layout.addSpacerItem(QtWidgets.QSpacerItem(20, 40))
        layout.addWidget(QLabel())
        splash.setLayout(layout)
        splash.showMessage(f'{data}', color=QColor(200, 200, 200))
        splash.show()
        QCoreApplication.processEvents()
        return splash

    return QSplashScreen()
