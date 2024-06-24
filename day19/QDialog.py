from PyQt5.QtWidgets import QApplication, QDialog

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Dialog')

if __name__ == '__main__':
    app = QApplication([])
    dialog = MyDialog()
    dialog.show()
    app.exec_()
