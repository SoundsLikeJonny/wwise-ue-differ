from unittest import TestCase
from src.engine.wwise import WAAPI
from src.ui.windows.ui_main_window import UIMainWindow

from PySide6.QtWidgets import (
    QApplication,
)


class TestUIMainWindow(TestCase):
    def setUp(self) -> None:
        app = QApplication()

        self.window = UIMainWindow()

    def tearDown(self) -> None:
        pass

    def test_load_csv_no_prompt(self):
        self.window.load_csv_no_prompt(
            '')
        self.assertTrue(True)

    def test_get_parse_wav_import_file(self):
        result = self.window.get_parse_wav_import_file('')
        self.assertEqual(result, result)

    def test_set_property(self):
        result = self.window.wwise.set_property('{16933D0C-9305-4AE3-8F49-9D03365F6D61}', 'IsStreamingEnabled', True)
