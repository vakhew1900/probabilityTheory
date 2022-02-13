from cProfile import label
from hashlib import new
from tkinter import Widget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
import combinatorics 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 300, 600, 400)
        self.setWindowTitle("Теория вероятностей 1 лабораторная")
        self.initUI()
        self.show()

    def initUI(self):
        
        centralWidget = QWidget()                          
        self.setCentralWidget(centralWidget)

        grid = QGridLayout()
        centralWidget.setLayout(grid)

        tabWidget = QTabWidget()
        movingWidget = self.initMoving()
        tabWidget.addTab(movingWidget, "Перемещение")
        
        grid.addWidget(tabWidget)

    def initMoving(self):
        widget = QWidget()
        vbox = QVBoxLayout()
        widget.setLayout(vbox)
       
        additWidget = QWidget()
        label = QLabel("Количество элементов:")
        lineEdit = QLineEdit()
        movingButton = QPushButton("Запустить")
        hbox = QHBoxLayout()
        additWidget.setLayout(hbox)
        hbox.addWidget(label)
        hbox.addWidget(lineEdit)
        hbox.addWidget(movingButton)
        hbox.setSpacing(15)
        
        img = QLabel(self)
        pixmap = QPixmap('1.jpg')
        img.setPixmap(pixmap)
        
        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        horizontalSpacer = QSpacerItem(160, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)

        hboxForImg = QHBoxLayout()
        hboxForImg.addItem(horizontalSpacer)
        hboxForImg.addWidget(img)
        hboxForImg.addItem(horizontalSpacer)
        imgWidget = QWidget() 
        imgWidget.setLayout(hboxForImg)

        ansWidget = QWidget()
        ansLabel = QLabel("перемещение:")
        ansLineEdit = QLineEdit() 
        hboxAnswer = QHBoxLayout()
        ansWidget.setLayout(hboxAnswer)
        hboxAnswer.addWidget(ansLabel)
        hboxAnswer.addWidget(ansLineEdit)

        vbox.addItem(horizontalSpacer)
        vbox.addItem(verticalSpacer)
        vbox.addWidget(imgWidget)
        vbox.addWidget(additWidget)
        vbox.addItem(verticalSpacer)
        vbox.addWidget(ansWidget)
        vbox.addItem(horizontalSpacer)

        movingButton.clicked.connect(lambda: self.P(lineEdit, ansLineEdit))
        return widget   

    def P(self, lineEdit, answerLineEdit):
        number = lineEdit.text()
        answer = combinatorics.P(int(number))
        answerLineEdit.setText(str(answer))
        
    
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())