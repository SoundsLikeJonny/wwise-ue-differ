from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet, list_themes


def set_default_theme(app: QApplication):
    app.setStyleSheet('')


def set_ose_theme(app: QApplication):
    apply_stylesheet(app, theme='dark_yellow.xml', extra=Defaults.EXTRA)


class Defaults:
    EXTRA = {'density_scale': '-2'}
