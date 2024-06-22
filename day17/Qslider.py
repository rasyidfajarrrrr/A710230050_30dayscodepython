from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.on_value_changed)

    def on_value_changed(self, value):
        print('Slider value:', value)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
