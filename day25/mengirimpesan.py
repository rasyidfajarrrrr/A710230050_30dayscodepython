import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class MessageApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Layout
        self.layout = QVBoxLayout()

        # Widgets
        self.message_label = QLabel("Enter your message:")
        self.message_input = QLineEdit()
        self.send_button = QPushButton("Send")
        self.display_label = QLabel("")

        # Add Widgets to Layout
        self.layout.addWidget(self.message_label)
        self.layout.addWidget(self.message_input)
        self.layout.addWidget(self.send_button)
        self.layout.addWidget(self.display_label)

        # Set Layout
        self.setLayout(self.layout)

        # Button Click Event
        self.send_button.clicked.connect(self.send_message)

        # Window settings
        self.setWindowTitle('Message Sender')
        self.show()

    def send_message(self):
        message = self.message_input.text()
        self.display_label.setText(f"Message sent: {message}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MessageApp()
    sys.exit(app.exec_())
