from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from Zekr_Statements import zekr


class Counter(QWidget):
    def __init__(self):
        super().__init__()
        self.zekr_idx = 0
        self.setWindowTitle("Counter")

        self.layout = QVBoxLayout()

        self.lbl = QLabel("0")
        self.lbl.setAlignment(Qt.AlignCenter)

        self.inc_button = QPushButton(zekr[self.zekr_idx])
        self.inc_button.clicked.connect(self.increment)

        self.layout.addWidget(self.lbl)
        self.layout.addWidget(self.inc_button)
        self.setLayout(self.layout)

    def increment(self):
        x = int(self.lbl.text())
        if x == 33:
            x = -1
            self.zekr_idx = (self.zekr_idx + 1) % len(zekr)
            if self.zekr_idx == 0:
                self.inc_button.setEnabled(False)
        self.inc_button.setText(zekr[self.zekr_idx])
        self.lbl.setText(str(x + 1))
