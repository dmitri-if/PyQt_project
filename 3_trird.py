import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal


lst_alita_1 = []
f = 0

class AlitaForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('alita_2.ui', self)  # Загружаем дизайн
        self.setFixedSize(893, 598)
        self.setWindowTitle('Alita')
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ailta')

        self.pixmap = QPixmap('images/alita.webp')
        self.pixmap.setDevicePixelRatio(1.9)
        self.label.setPixmap(self.pixmap)

        self.zal1.clicked.connect(self.open_zal1)
        self.back.clicked.connect(self.close)
    
    def open_zal1(self):
        self.tree_form = Zal1(self, 'Alita')
        self.tree_form.show()

class Zal1(QMainWindow):
    def __init__(self, *args):
        global lst_alita_1
        self.args = args[1]
        super().__init__()
        uic.loadUi('typepasad/1type_trird.ui', self)  # Загружаем дизайн
        self.setWindowTitle('Zal1')
        self.setFixedSize(765, 670)
        self.initUI()

    def initUI(self):
        self.lst = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5, 
                self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10, 
                self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14, self.pushButton_15, 
                self.pushButton_16, self.pushButton_17, self.pushButton_18, self.pushButton_19, self.pushButton_20, 
                self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24, self.pushButton_25, 
                self.pushButton_26, self.pushButton_27, self.pushButton_28, self.pushButton_29, self.pushButton_30,  
                self.pushButton_31, self.pushButton_32, self.pushButton_33, self.pushButton_34, self.pushButton_35,  
                self.pushButton_36, self.pushButton_37, self.pushButton_38]
        for i in lst_alita_1:
            self.lst[i-1].setEnabled(False)

        # Соединение кнопок
        self.pay.clicked.connect(self.pay_ticket)
        self.back.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.btn)
        self.pushButton_2.clicked.connect(self.btn2)
        self.pushButton_3.clicked.connect(self.btn3)
        self.pushButton_4.clicked.connect(self.btn4)
        self.pushButton_5.clicked.connect(self.btn5)
        self.pushButton_6.clicked.connect(self.btn6)
        self.pushButton_7.clicked.connect(self.btn7)
        self.pushButton_8.clicked.connect(self.btn8)
        self.pushButton_9.clicked.connect(self.btn9)
        self.pushButton_10.clicked.connect(self.btn10)
        self.pushButton_11.clicked.connect(self.btn11)
        self.pushButton_12.clicked.connect(self.btn12)
        self.pushButton_13.clicked.connect(self.btn13)
        self.pushButton_14.clicked.connect(self.btn14)
        self.pushButton_15.clicked.connect(self.btn15)
        self.pushButton_16.clicked.connect(self.btn16)
        self.pushButton_17.clicked.connect(self.btn17)
        self.pushButton_18.clicked.connect(self.btn18)
        self.pushButton_19.clicked.connect(self.btn19)
        self.pushButton_20.clicked.connect(self.btn20)
        self.pushButton_21.clicked.connect(self.btn21)
        self.pushButton_22.clicked.connect(self.btn22)
        self.pushButton_23.clicked.connect(self.btn23)
        self.pushButton_24.clicked.connect(self.btn24)
        self.pushButton_25.clicked.connect(self.btn25)
        self.pushButton_26.clicked.connect(self.btn26)
        self.pushButton_27.clicked.connect(self.btn27)
        self.pushButton_28.clicked.connect(self.btn28)
        self.pushButton_29.clicked.connect(self.btn29)
        self.pushButton_30.clicked.connect(self.btn30)
        self.pushButton_31.clicked.connect(self.btn31)
        self.pushButton_32.clicked.connect(self.btn32)
        self.pushButton_33.clicked.connect(self.btn33)
        self.pushButton_34.clicked.connect(self.btn34)
        self.pushButton_35.clicked.connect(self.btn35)
        self.pushButton_36.clicked.connect(self.btn36)
        self.pushButton_37.clicked.connect(self.btn37)
        self.pushButton_38.clicked.connect(self.btn38)
        # for i in range(2, 39):
        #             print(f'def btn{i}(self):\n\tif self.pushButton_{i}.text() == "{i}":\n\tself.pushButton_{i}.setText("|{i}|")\n\telse:\n\tself.pushButton_{i}.setText("{i}")')
    
    def pay_ticket(self):
        self.second_form = PayForm()
        self.second_form.show()
        self.second_form.closed.connect(self.check)
           
    def check(self):
        global lst_alita_1, f
        if f:
            for i in self.lst:
                if i.text()[0] == '|':
                    if self.lst.index(i) + 1 not in lst_alita_1:
                        lst_alita_1.append(self.lst.index(i) + 1)
                        i.setEnabled(False)
                f = 0

    # Функции кнопок
    def btn(self):
        if self.pushButton.text() == '1':
            self.pushButton.setText('|1|')
        else:
            self.pushButton.setText('1')
    
    def btn2(self):
        if self.pushButton_2.text() == "2":
            self.pushButton_2.setText("|2|")
        else:
            self.pushButton_2.setText("2")

    def btn3(self):
        if self.pushButton_3.text() == "3":
            self.pushButton_3.setText("|3|")
        else:
            self.pushButton_3.setText("3")

    def btn4(self):
        if self.pushButton_4.text() == "4":
            self.pushButton_4.setText("|4|")
        else:
            self.pushButton_4.setText("4")

    def btn5(self):
        if self.pushButton_5.text() == "5":
            self.pushButton_5.setText("|5|")
        else:
            self.pushButton_5.setText("5")

    def btn6(self):
        if self.pushButton_6.text() == "6":
            self.pushButton_6.setText("|6|")
        else:
            self.pushButton_6.setText("6")

    def btn7(self):
        if self.pushButton_7.text() == "7":
            self.pushButton_7.setText("|7|")
        else:
            self.pushButton_7.setText("7")

    def btn8(self):
        if self.pushButton_8.text() == "8":
            self.pushButton_8.setText("|8|")
        else:
            self.pushButton_8.setText("8")

    def btn9(self):
        if self.pushButton_9.text() == "9":
            self.pushButton_9.setText("|9|")
        else:
            self.pushButton_9.setText("9")

    def btn10(self):
        if self.pushButton_10.text() == "10":
            self.pushButton_10.setText("|10|")
        else:
            self.pushButton_10.setText("10")

    def btn11(self):
        if self.pushButton_11.text() == "11":
            self.pushButton_11.setText("|11|")
        else:
            self.pushButton_11.setText("11")

    def btn12(self):
        if self.pushButton_12.text() == "12":
            self.pushButton_12.setText("|12|")
        else:
            self.pushButton_12.setText("12")

    def btn13(self):
        if self.pushButton_13.text() == "13":
            self.pushButton_13.setText("|13|")
        else:
            self.pushButton_13.setText("13")

    def btn14(self):
        if self.pushButton_14.text() == "14":
            self.pushButton_14.setText("|14|")
        else:
            self.pushButton_14.setText("14")

    def btn15(self):
        if self.pushButton_15.text() == "15":
            self.pushButton_15.setText("|15|")
        else:
            self.pushButton_15.setText("15")

    def btn16(self):
        if self.pushButton_16.text() == "16":
            self.pushButton_16.setText("|16|")
        else:
            self.pushButton_16.setText("16")

    def btn17(self):
        if self.pushButton_17.text() == "17":
            self.pushButton_17.setText("|17|")
        else:
            self.pushButton_17.setText("17")

    def btn18(self):
        if self.pushButton_18.text() == "18":
            self.pushButton_18.setText("|18|")
        else:
            self.pushButton_18.setText("18")

    def btn19(self):
        if self.pushButton_19.text() == "19":
            self.pushButton_19.setText("|19|")
        else:
            self.pushButton_19.setText("19")

    def btn20(self):
        if self.pushButton_20.text() == "20":
            self.pushButton_20.setText("|20|")
        else:
            self.pushButton_20.setText("20")

    def btn21(self):
        if self.pushButton_21.text() == "21":
            self.pushButton_21.setText("|21|")
        else:
            self.pushButton_21.setText("21")

    def btn22(self):
        if self.pushButton_22.text() == "22":
            self.pushButton_22.setText("|22|")
        else:
            self.pushButton_22.setText("22")

    def btn23(self):
        if self.pushButton_23.text() == "23":
            self.pushButton_23.setText("|23|")
        else:
            self.pushButton_23.setText("23")

    def btn24(self):
        if self.pushButton_24.text() == "24":
            self.pushButton_24.setText("|24|")
        else:
            self.pushButton_24.setText("24")

    def btn25(self):
        if self.pushButton_25.text() == "25":
            self.pushButton_25.setText("|25|")
        else:
            self.pushButton_25.setText("25")

    def btn26(self):
        if self.pushButton_26.text() == "26":
            self.pushButton_26.setText("|26|")
        else:
            self.pushButton_26.setText("26")

    def btn27(self):
        if self.pushButton_27.text() == "27":
            self.pushButton_27.setText("|27|")
        else:
            self.pushButton_27.setText("27")

    def btn28(self):
        if self.pushButton_28.text() == "28":
            self.pushButton_28.setText("|28|")
        else:
            self.pushButton_28.setText("28")

    def btn29(self):
        if self.pushButton_29.text() == "29":
            self.pushButton_29.setText("|29|")
        else:
            self.pushButton_29.setText("29")

    def btn30(self):
        if self.pushButton_30.text() == "30":
            self.pushButton_30.setText("|30|")
        else:
            self.pushButton_30.setText("30")

    def btn31(self):
        if self.pushButton_31.text() == "31":
            self.pushButton_31.setText("|31|")
        else:
            self.pushButton_31.setText("31")

    def btn32(self):
        if self.pushButton_32.text() == "32":
            self.pushButton_32.setText("|32|")
        else:
            self.pushButton_32.setText("32")

    def btn33(self):
        if self.pushButton_33.text() == "33":
            self.pushButton_33.setText("|33|")
        else:
            self.pushButton_33.setText("33")

    def btn34(self):
        if self.pushButton_34.text() == "34":
            self.pushButton_34.setText("|34|")
        else:
            self.pushButton_34.setText("34")

    def btn35(self):
        if self.pushButton_35.text() == "35":
            self.pushButton_35.setText("|35|")
        else:
            self.pushButton_35.setText("35")

    def btn36(self):
        if self.pushButton_36.text() == "36":
            self.pushButton_36.setText("|36|")
        else:
            self.pushButton_36.setText("36")

    def btn37(self):
        if self.pushButton_37.text() == "37":
            self.pushButton_37.setText("|37|")
        else:
            self.pushButton_37.setText("37")

    def btn38(self):
        if self.pushButton_38.text() == "38":
            self.pushButton_38.setText("|38|")
        else:
            self.pushButton_38.setText("38")


class PayForm(QMainWindow):
    closed = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi('pay.ui', self)
        self.hintLabel.setText('Введите номер карты (16 цифр без пробелов):')
        self.payButton.clicked.connect(self.process_data)
        self.back.clicked.connect(self.close)
        self.setWindowTitle('Pay')
        self.setFixedSize(709, 170)

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)
    
    def get_card_number(self):
        card_num = self.cardData.text()
        card_num = ''.join(card_num.split())
        if card_num.isdigit() and len(card_num) == 16:
            return card_num
        else:
            return 404

    def double(self, x):
        res = x * 2
        if res > 9:
            res = res - 9
        return res

    def luhn_algorithm(self, card):
        odd = map(lambda x: self.double(int(x)), card[::2])
        even = map(int, card[1::2])
        return (sum(odd) + sum(even)) % 10 == 0

    def process_data(self):
        global f
        number = self.get_card_number()
        if number == 404:
            self.errorLabel.setText(
                "Введите только 16 цифр. Допускаются пробелы")
        elif self.luhn_algorithm(number):
            self.errorLabel.setText(
                "Ваша карта обрабатывается...")
        else:
            f = 1
            self.close()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlitaForm()
    ex.show()
    sys.exit(app.exec())