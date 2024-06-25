from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Membuat QListWidget
        self.list_widget = QListWidget()

        # Menambahkan item ke QListWidget
        self.list_widget.addItem('Alice')
        self.list_widget.addItem('Bob')
        self.list_widget.addItem('Charlie')

        self.setCentralWidget(self.list_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
