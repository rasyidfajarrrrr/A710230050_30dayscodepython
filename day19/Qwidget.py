from PyQt5.QtWidgets import QApplication, QWidget

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Form')

app = QApplication([])
form = MyForm()
form.show()
app.exec_()
