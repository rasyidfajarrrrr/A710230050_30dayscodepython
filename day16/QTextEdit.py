from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit(self)
        self.textEdit.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        print('Text changed')

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
