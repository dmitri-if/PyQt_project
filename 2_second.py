import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


class PayForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pay.ui', self)
        self.hintLabel.setText('Введите номер карты (16 цифр без пробелов):')
        self.payButton.clicked.connect(self.process_data)
    
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
        number = self.get_card_number()
        if number == 404:
            self.errorLabel.setText(
                "Введите только 16 цифр. Допускаются пробелы")
        elif self.luhn_algorithm(number):
            self.errorLabel.setText(
                "Ваша карта обрабатывается...")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PayForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())