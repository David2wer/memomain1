from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup, QSpinBox

def ans():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    btn_answer.clicked.connect(quest)
def quest():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_answer.clicked.connect(ans)
app = QApplication([])

w = QWidget()
w.setWindowTitle("Memory Card")
w.move(30,60)
w.resize(600, 500)


layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2= QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4= QHBoxLayout()
layoutH5 = QHBoxLayout()
layoutH6= QHBoxLayout()


btn_answer = QPushButton("Відповісти")
btn_Menu = QPushButton("Меню")
btn_Sleep = QPushButton("Відпочити")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_Ok = QPushButton("Ответить")
question = QLabel("Яблуко")
question1 = QLabel("хвилин")



RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()

btn_answer1 = QRadioButton("building")
btn_answer2 = QRadioButton("aplication")
btn_answer3 = QRadioButton("caterpillar")
btn_answer4 = QRadioButton("apple")

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("Win")
lb_Correct = QLabel("Lose")
layout_res = QVBoxLayout()
#layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
#layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, scretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)
layoutH1.addWidget(btn_Menu,alignment = Qt.AlignLeft)
layoutH2.addWidget(question, alignment = Qt.AlignCenter)
layoutH1.addWidget(btn_Sleep, alignment = Qt.AlignRight)
layoutH1.addWidget(box_Minutes, alignment = Qt.AlignRight)
layoutH1.addWidget(question1, alignment = Qt.AlignRight)
layoutH4.addWidget(btn_answer, alignment = Qt.AlignCenter)



layoutH3.addWidget(RadioGroupBox)
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.addLayout(layoutH4)

w.setLayout(layout_main)
layout_ansV = QVBoxLayout()
layout_ansH1 = QHBoxLayout()
layout_ansH2 = QHBoxLayout()

layout_ansH1.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layout_ansH1.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layout_ansH2.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layout_ansH2.addWidget(btn_answer4, alignment = Qt.AlignCenter)

layout_ansV.addLayout(layout_ansH1)
layout_ansV.addLayout(layout_ansH2)

RadioGroupBox.setLayout(layout_ansV)

btn_answer.clicked.connect(ans)
w.show()
app.exec_()




