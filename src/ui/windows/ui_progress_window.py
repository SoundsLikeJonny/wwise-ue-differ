from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal

from src.ui.gui import ProgressWindow


class ProgressBarWindow(QDialog, ProgressWindow.Ui_Dialog):
    signal_window_closed = Signal()

    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.setupUi(self)

    def close(self) -> None:
        super().close()
