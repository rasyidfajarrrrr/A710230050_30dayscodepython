from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.label = QLabel('Hello PyQt!', self)
        self.label.adjustSize()

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
