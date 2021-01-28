from ui import UI
from data_manager import DataManager


class App:
    def __init__(self):
        self.ui = UI(DataManager())
        # self.data_manager = DataManager()

    def start(self):
        self.ui.mainloop()
        # print(self.data_manager.load_data())
