import sys

from userUi import Ui_UserMain
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class UserWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_UserMain()
        self.ui.setupUi(self)
        self.center()

    # centralizar tela
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user = UserWindow()
    user.show()
    app.exec_()
