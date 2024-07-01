# form.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from database import create_table, add_user, get_users

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Data Pengguna")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.name_label = QLabel("Nama:")
        self.name_input = QLineEdit()

        self.age_label = QLabel("Umur:")
        self.age_input = QLineEdit()

        self.submit_button = QPushButton("Simpan Data")
        self.submit_button.clicked.connect(self.submit_data)

        self.show_data_button = QPushButton("Tampilkan Data")
        self.show_data_button.clicked.connect(self.show_data)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.show_data_button)

        self.central_widget.setLayout(self.layout)

    def submit_data(self):
        name = self.name_input.text()
        age = self.age_input.text()

        if name and age.isdigit():
            add_user(name, int(age))
            QMessageBox.information(self, "Berhasil", "Data berhasil disimpan.")
            self.name_input.clear()
            self.age_input.clear()
        else:
            QMessageBox.warning(self, "Gagal", "Masukkan nama dan umur yang valid.")

    def show_data(self):
        users = get_users()
        message = "Data Pengguna:\n"
        for user in users:
            message += f"ID: {user[0]}, Nama: {user[1]}, Umur: {user[2]}\n"
        QMessageBox.information(self, "Data Pengguna", message)

if __name__ == "__main__":
    create_table()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
