import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from view.sobreUi import Ui_Form


class SobreWindow(QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sobre = SobreWindow()
    sobre.show()
    app.exec_()
