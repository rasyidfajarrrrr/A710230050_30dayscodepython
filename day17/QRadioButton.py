from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.radioButton = QRadioButton('Select Me', self)
        self.radioButton.toggled.connect(self.on_toggled)

    def on_toggled(self, is_checked):
        if is_checked:
            print('Selected')

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
