import sys
from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Yaxshi")
    cancel = QtWidgets.QPushButton("Leghv et")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
   

    v_box = QtWidgets.QVBoxLayout()

    v_box.addStretch()
    v_box.addLayout(h_box)
    
    # v_box.addWidget(okay)
    # v_box.addWidget(cancel)
    

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 4")
    
    pencere.setLayout(v_box)

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())

Pencere()