from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class Counter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Counter")

        self.layout = QVBoxLayout()

        self.lbl = QLabel("0")
        self.lbl.setAlignment(Qt.AlignCenter)

        self.inc_button = QPushButton("سبحان الله")
        # self.dec_button = QPushButton("-")

        # self.dec_button.clicked.connect(self.decrement)
        self.inc_button.clicked.connect(self.increment)

        # self.layout.addWidget(self.dec_button)
        self.layout.addWidget(self.lbl)
        self.layout.addWidget(self.inc_button)
        self.setLayout(self.layout)

    def increment(self):
        x = int(self.lbl.text())
        if x == 33:
            x = -1
            match self.inc_button.text():
                case "سبحان الله":
                    self.inc_button.setText("الحمد لله")
                case "الحمد لله":
                    self.inc_button.setText("الله أكبر")
                case _:
                    self.inc_button.setText("سبحان الله")
                    self.inc_button.setEnabled(False)
        self.lbl.setText(str(x + 1))
