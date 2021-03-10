from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from gui_simple_designer import Ui_MainWindow
import os
import replay
import config as cfg


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.buttonLoad.clicked.connect(self.load_replay)
        self.buttonRun.clicked.connect(self.extract_build_order)
        self.setWindowTitle(f"ElementTD 2 Build Order Extractor v{cfg.version_string}")
        self.pfn_replay = None
        self.replay = replay.Replay()

    def load_replay(self):
        self.pfn_replay = QFileDialog.getOpenFileName(self,
                                                      'Load file',
                                                      os.path.join(os.getenv('APPDATA'), "..\\LocalLow\\Element Studios\\Element TD 2"),
                                                      "json files (*.json)")
        self.replay.load_replay_data(self.pfn_replay[0])
        player_list = self.replay.get_available_players()
        self.cbSelectPlayer.clear()
        self.cbSelectPlayer.addItems(player_list)
        pass

    def extract_build_order(self):
        if self.cbSelectPlayer.currentText() == "<-- load replay first":
            self.show_now_player_selected_popup()
            return

        selected_player_id = self.cbSelectPlayer.currentIndex()
        self.outputField.setPlainText(self.replay.get_build_order(player_id=selected_player_id))

    def show_now_player_selected_popup(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Warning")
        msg.setText("Please load a replay and select a player first.")
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
