from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        layout.addWidget(QPushButton('Button 1'), 0, 0)
        layout.addWidget(QPushButton('Button 2'), 0, 1)
        layout.addWidget(QPushButton('Button 3'), 1, 0)
        layout.addWidget(QPushButton('Button 4'), 1, 1)
        layout.addWidget(QPushButton('Button 5'), 2, 0, 1, 2)

        self.setLayout(layout)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
