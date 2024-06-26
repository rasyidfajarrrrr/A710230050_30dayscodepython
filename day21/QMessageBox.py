from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        button = QPushButton("Show Message")
        button.clicked.connect(self.show_message)
        self.setCentralWidget(button)

    def show_message(self):
        QMessageBox.information(self, "Hello!", "This is a message.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
