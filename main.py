from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Mod Publisher Pro (Open source)")

counter = 0

# Create a label
label = QLabel(window)
label.setText("Counter: " + str(counter))
label.move(50, 50)
label.setFont(QFont("Calibri", 20))

# Create a button
button = QPushButton(window)
button.setText("Click me!")
button.move(50, 100)

def OnButtonClicked():
    global counter

    print("Hello World!")
    counter += 1
    label.setText("Counter: " + str(counter))
    label.adjustSize()

button.clicked.connect(OnButtonClicked)

# Show window

window.show()

app.exec()