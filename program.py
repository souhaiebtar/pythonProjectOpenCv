import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Qt Window")
        self.setGeometry(100, 100, 400, 300)

        # Create a label
        self.label = QLabel("Hello, Qt!")

        # Create a layout and add the label to it
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())