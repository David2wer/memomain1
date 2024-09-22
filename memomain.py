from memodata import*
from project import*
from memoeditlayout import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import* 
app = QApplication([])
win = QWidget()
win.setFixedSize(1000,500)
win.move(0,0)

win.show()
app.exec_