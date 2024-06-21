from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton('Click Me!', self)
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print('Button clicked!')

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
