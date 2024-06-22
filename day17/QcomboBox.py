from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(['Option 1', 'Option 2', 'Option 3'])
        self.comboBox.currentIndexChanged.connect(self.on_index_changed)

    def on_index_changed(self, index):
        print('Selected option:', self.comboBox.itemText(index))

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
