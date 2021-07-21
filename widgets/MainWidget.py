import PySide6.QtWidgets as QtWidgets


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton()
        self.text = QtWidgets.QLabel()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)

        self.button.clicked.connect(self.magic)
        self.state = {
            "numClicks": 0
        }

        self.text.setText("hello world")
        self.button.setText("click me")

    def magic(self):
        self.state["numClicks"] += 1
        self.text.setText("hello world" + str(self.state["numClicks"]))
