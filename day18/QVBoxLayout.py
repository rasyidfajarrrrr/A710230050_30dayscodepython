from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QPushButton('Button 1'))
        layout.addWidget(QPushButton('Button 2'))
        layout.addWidget(QPushButton('Button 3'))

        self.setLayout(layout)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
