import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider, QComboBox)
from PyQt5.QtCore import Qt

class RemoteAC(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Remote AC')
        self.setGeometry(100, 100, 300, 200)  # Atur ukuran window

        # Layout utama
        mainLayout = QVBoxLayout()

        # Label untuk status AC
        self.statusLabel = QLabel('AC is OFF', self)
        self.statusLabel.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(self.statusLabel)

        # Tombol untuk menyalakan dan mematikan AC
        buttonLayout = QHBoxLayout()
        
        self.onButton = QPushButton('Turn ON', self)
        self.onButton.clicked.connect(self.turn_on)
        buttonLayout.addWidget(self.onButton)

        self.offButton = QPushButton('Turn OFF', self)
        self.offButton.clicked.connect(self.turn_off)
        buttonLayout.addWidget(self.offButton)
        
        mainLayout.addLayout(buttonLayout)

        # Slider untuk mengatur suhu
        tempLayout = QHBoxLayout()
        self.tempLabel = QLabel('Temperature: 24°C', self)
        tempLayout.addWidget(self.tempLabel)
        
        self.tempSlider = QSlider(Qt.Horizontal)
        self.tempSlider.setMinimum(16)
        self.tempSlider.setMaximum(30)
        self.tempSlider.setValue(24)
        self.tempSlider.valueChanged.connect(self.change_temperature)
        tempLayout.addWidget(self.tempSlider)

        mainLayout.addLayout(tempLayout)

        # ComboBox untuk memilih mode AC
        modeLayout = QHBoxLayout()
        self.modeLabel = QLabel('Mode: Cool', self)
        modeLayout.addWidget(self.modeLabel)

        self.modeComboBox = QComboBox()
        self.modeComboBox.addItems(['Cool', 'Heat', 'Fan'])
        self.modeComboBox.currentTextChanged.connect(self.change_mode)
        modeLayout.addWidget(self.modeComboBox)

        mainLayout.addLayout(modeLayout)

        self.setLayout(mainLayout)

    def turn_on(self):
        self.statusLabel.setText('AC is ON')

    def turn_off(self):
        self.statusLabel.setText('AC is OFF')

    def change_temperature(self):
        temp = self.tempSlider.value()
        self.tempLabel.setText(f'Temperature: {temp}°C')

    def change_mode(self):
        mode = self.modeComboBox.currentText()
        self.modeLabel.setText(f'Mode: {mode}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    remote = RemoteAC()
    remote.show()
    sys.exit(app.exec_())
