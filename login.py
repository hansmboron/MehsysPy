import sqlite3
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMessageBox, QMainWindow, QStyle

from view.loginUi import Ui_TelaLoginUi
from principal import PrincipalWindow
from Utils.criaBdSqlite import CreateBdSqlite


class LoginWindow(QMainWindow, Ui_TelaLoginUi):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.btnEntrar.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DialogApplyButton')))
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        # self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'img/logo_peq.png'))

        self.center()

        #  connect evento de botao
        self.btnEntrar.clicked.connect(self.login)

    # centralizar tela
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #  Função do botão entrar
    def login(self):
        # conectar no bando de dados
        self.db = sqlite3.connect('dbmehsys.db')
        self.cursor = self.db.cursor()
        sql = "select * from tbusuarios where login=? and senha=?"
        user = self.txtUser.text()
        password = self.txtPass.text()
        self.cursor.execute(sql, [user, password])
        rs = self.cursor.fetchall()
        if len(user) < 1 or len(password) < 1:
            QMessageBox.warning(self, "Erro ao Logar", "PREENCHA OS CAMPOS LOGIN E SENHA PARA ENTRAR\n\n\nObs: "
                                                       "Usuário padrão(admin), "
                                                       "Senha padrão(1234)", QMessageBox.Ok,
                                QMessageBox.Ok)
        elif len(rs) > 0:
            id_user = str(rs[0][0])
            self.cursor.execute('insert into utils (current_user) values (?)', [id_user])
            self.db.commit()
            if rs[0][5] == 'admin':  # Se perfil == 'admin'
                self.window = PrincipalWindow()
                self.window.show()
                self.window.actionAddHor.setEnabled(True)
                self.window.actionUsu_rios.setEnabled(True)
                self.window.actionClientes_2.setEnabled(True)
                self.window.actionHor_rios_2.setEnabled(True)
                self.window.actionServi_os_2.setEnabled(True)
                self.cursor.close()
                self.db.close()
                login.close()
            else:  # perfil == 'user'
                self.window = PrincipalWindow()
                self.window.show()
                self.cursor.close()
                self.db.close()
                login.close()
        else:
            QMessageBox.warning(self, "Erro ao Logar",
                                "USUÁRIO OU SENHA INVÁLIDO(S)\n\n\nObs: Usuário padrão(admin), "
                                "Senha padrão(1234)", QMessageBox.Ok,
                                QMessageBox.Ok)

    # eventos do teclado
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.login()
        if event.key() == Qt.Key_Down:
            self.txtPass.setFocus()
        if event.key() == Qt.Key_Up:
            self.txtUser.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()
    bd = CreateBdSqlite()
    bd.create_tables()
    login.show()
    app.exec_()
