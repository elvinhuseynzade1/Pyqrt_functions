import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.yazi_yeri = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yaz = QtWidgets.QPushButton("Yaz")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazi_yeri)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yaz)
        v_box.addStretch()

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.click)
        self.yaz.clicked.connect(self.click)

        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Temizle":
            self.yazi_yeri.clear()

        else:
            print(self.yazi_yeri.text())




app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

