import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class Converter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Masukkan bilangan desimal:")
        self.layout.addWidget(self.label)
        
        self.input_line = QLineEdit(self)
        self.layout.addWidget(self.input_line)
        
        self.convert_button = QPushButton("Konversi", self)
        self.convert_button.clicked.connect(self.convert_number)
        self.layout.addWidget(self.convert_button)
        
        self.result_label = QLabel("Hasil:")
        self.layout.addWidget(self.result_label)
        
        self.setLayout(self.layout)
        self.setWindowTitle("Konversi Bilangan")
        self.show()
        
    def convert_number(self):
        try:
            num = int(self.input_line.text())
            bin_result = bin(num)[2:]
            oct_result = oct(num)[2:]
            hex_result = hex(num)[2:].upper()
            
            result_text = f"Biner: {bin_result}\nOktal: {oct_result}\nHeksadesimal: {hex_result}"
            self.result_label.setText(result_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Masukkan bilangan desimal yang valid")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Converter()
    sys.exit(app.exec_())
