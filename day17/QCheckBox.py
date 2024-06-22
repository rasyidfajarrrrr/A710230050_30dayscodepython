from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.checkBox = QCheckBox('Check Me', self)
        self.checkBox.stateChanged.connect(self.on_state_changed)

    def on_state_changed(self, state):
        if state == Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
