from PyQt5.QtWidgets import QApplication
import sys

from GUI.frame.main_window import MainWindow

class App(QApplication):
    def __init__(self):
        super(App, self).__init__(sys.argv)
        self.main_window = MainWindow()
        self.main_window.show()

