import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Konversi Suhu')

        layout = QVBoxLayout()

        self.input_label = QLabel('Masukkan suhu dalam Celsius:')
        layout.addWidget(self.input_label)

        self.input_edit = QLineEdit(self)
        layout.addWidget(self.input_edit)

        self.result_label = QLabel('Suhu dalam Fahrenheit:')
        layout.addWidget(self.result_label)

        self.result_display = QLabel('')
        layout.addWidget(self.result_display)

        self.convert_button = QPushButton('Konversi', self)
        self.convert_button.clicked.connect(self.konversi_suhu)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

    def konversi_suhu(self):
        try:
            celsius = float(self.input_edit.text())
            fahrenheit = (celsius * 9/5) + 32
            self.result_display.setText(f'{fahrenheit} °F')
        except ValueError:
            self.result_display.setText('Input tidak valid!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KonversiSuhu()
    ex.show()
    sys.exit(app.exec_())
