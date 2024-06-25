from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Membuat model
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Age'])

        # Menambahkan data ke model
        names = ['Alice', 'Bob', 'Charlie']
        ages = [25, 32, 18]
        for i in range(3):
            name_item = QStandardItem(names[i])
            age_item = QStandardItem(str(ages[i]))
            self.model.appendRow([name_item, age_item])

        # Membuat QTableView dan mengatur modelnya
        self.table = QTableView()
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
