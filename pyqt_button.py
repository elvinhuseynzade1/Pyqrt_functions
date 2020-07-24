import sys
from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 3")

    button = QtWidgets.QPushButton(pencere)
    button.setText("Here is button")
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Hello")
    
    etiket.move(220,30)
    button.move(180,80)

    pencere.setGeometry(100,100,500,500)
    pencere.show()

    sys.exit(app.exec_())

Pencere()