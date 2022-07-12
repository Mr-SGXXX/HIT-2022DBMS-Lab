import sys

from GUI import APP
from SQL.insert_data import *

if __name__ == "__main__":
    App = APP.App()
    sys.exit(App.exec())
