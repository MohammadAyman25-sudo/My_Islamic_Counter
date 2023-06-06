from PySide6.QtWidgets import QApplication
from Counter import Counter
import sys

app = QApplication(sys.argv)

win = Counter()
win.show()

app.exec()
