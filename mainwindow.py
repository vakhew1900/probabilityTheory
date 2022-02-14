from PyQt5 import QtWidgets
from design import Ui_MainWindow  
from PyQt5.QtGui import QPixmap, QIcon
import sys

def proiz(l, r):
    num = 1
    for i in range(l,r+1):
        num*=i
    return  num

def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num

def ARepeat(n, k):
    return (n ** k)

def P(n):
    return proiz(1, n)


def C(n, k):
    if(k > n - k):
        return proiz(k + 1, n) // proiz(1, n - k)
    else:
        return  proiz(n - k + 1, n) // proiz(1, k)

def therver2(n, k):
    res = 1
    length = len(k)
    for i in range(length):
        k_cur = k[i]
        n_cur = n[i]
        print(k[i]," ",n[i])
        res *= C(k[i], n[i])
    
    K = sum(k, start= 0)
    N = sum(n, start= 0)
    print(K, " ", N)
    print(res)
    res /= C(K, N)
    # print(res)
    return res

def CRepeat(n, k):
    return C(n + k - 1, k)

def therver(n, m):
    return C(n, m) / CRepeat(n, m)


    

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        mip = QPixmap('./image/combination.jpg')
        self.ui.imgLabel.setPixmap(mip)
        

        self.ui.comboBox.currentIndexChanged.connect(self.changeWidget)
        self.ui.pushButton.clicked.connect(self.doOperation)

    
    def changeWidget(self, index):
        
        if (index == 2):
            self.ui.mLineEdit.setVisible(False)
            self.ui.mLabel.setVisible(False)
            self.ui.mLineEdit.setText(str(1))
        else:
            self.ui.mLineEdit.setVisible(True)
            self.ui.mLabel.setVisible(True)

        mip = 0
        if(index == 0):
            mip = QPixmap('./image/combination.jpg')
        elif(index == 1):
            mip = QPixmap('./image/therver.jpg')
        elif(index == 2):
            mip = QPixmap('./image/moving.jpg')
        elif(index == 3):
            mip = QPixmap('./image/replace.png')
        elif(index == 4):
            mip = QPixmap('./image/therver.jpg')

        self.ui.imgLabel.setPixmap(mip)
        
        

    

    def doOperation(self):
        index = self.ui.comboBox.currentIndex()
        n  = 0
        m = 0
        ans = 0
        error = 0
        try:
            n = int(self.ui.nLinEdit.text())
        except:
            error = 1

        try:
            m = int(self.ui.mLineEdit.text())
        except:
            error  = 1

        # print(index)
        if(error == 1 and index != 4):
            ans = "ошибка ввода"
        elif(index == 0):
            ans = C(n, m)
        elif (index == 1):
            ans = therver(n, m)
        elif (index == 2):
            ans = P(n)
        elif (index == 3):
            ans = ARepeat(n, m)
        elif (index == 4):
           ans =  self.task5()

        self.ui.answerLineEdit.setText(str(ans))
            
    def task5(self):
        error = 0
        # print("this")
        try:
            # print('ddd\n')
            nLineEdit = self.ui.nLinEdit.text().split(sep =" ")
            mLineEdit = self.ui.mLineEdit.text().split(sep = " ")
            print(nLineEdit)
            n = list(map(int, nLineEdit))
            m = list(map(int, mLineEdit))
            print(n)
        except:
            error = 1
        
        if (error == 1):
             return "ошибка ввода"

        if (len(m) != len(n)):
            return "разное количество n и m"
        
        for i in range(len(m)):
            if n[i] > m[i]:
                return "m > n"
        ans = therver2(n, m)
        return ans
    

app = QtWidgets.QApplication([])
application = Window()
application.setWindowIcon(QIcon("./image/icon.jpg"))
application.show()
 
sys.exit(app.exec())