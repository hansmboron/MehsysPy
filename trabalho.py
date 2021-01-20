import os
import sqlite3
import sys

from PyQt5.QtCore import QTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox
from view.trabalhoUi import Ui_Form


class TrabalhoWindow(QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'img/logo_peq.png'))
        self.popula_lista()

        self.center()

        self.btnLim_tim.clicked.connect(self.on_btn_limpar_pressed)
        self.btnAdd_hor.clicked.connect(self.on_btn_add_pressed)
        self.btnDel_hor.clicked.connect(self.on_btn_del_pressed)
        self.listTra.clicked.connect(self.setar_campo)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_btn_limpar_pressed(self):
        self.timHor.setTime(QTime(0, 0))

    def popula_lista(self):
        self.listTra.clear()
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select horario from horarios order by horario'
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
            for i in range(len(rs)):
                self.listTra.addItem(rs[i][0])
            cursor.close()
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    def setar_campo(self):
        selected = self.listTra.currentItem().text()
        hor = int(selected[0:2])
        min = int(selected[3:5])
        self.timHor.setTime(QTime(hor, min))

    def on_btn_add_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'insert into horarios (horario) values (?)'
        horario = self.timHor.text()
        try:
            cursor.execute(sql, [horario])
            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            cursor.close()
            db.close()
            QMessageBox.critical(self, 'ERRO!!!', f'ESTE HORÁRIO JÁ FOI ADICIONADO!\n\n"{str(e)}"')
        self.on_btn_limpar_pressed()
        self.popula_lista()

    def on_btn_del_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'delete from horarios where horario=?'
        horario = self.timHor.text()
        try:
            cursor.execute(sql, [horario])
            db.commit()
            cursor.close()
        except Exception as e:
            cursor.close()
            db.close()
            QMessageBox.critical(self, 'ERRO!!!', f'HORÁRIO NÃO ENCONTRADO NO BANCO DE DADOS!\n\n"{str(e)}"')
        self.on_btn_limpar_pressed()
        self.popula_lista()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    trabalho = TrabalhoWindow()
    trabalho.show()
    app.exec_()
