from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lineEdit = QLineEdit(self)
        self.lineEdit.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, text):
        print('Text changed:', text)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
