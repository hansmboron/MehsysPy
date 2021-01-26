import sqlite3
import sys

import bcrypt
from PyQt5.QtCore import QTime

from Utils.readOnly import ReadOnlyDelegate
from view.userUi import Ui_UserMain
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QMessageBox, QTableWidgetItem


class UserWindow(QMainWindow, Ui_UserMain):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        # centralizar tela
        self.center()
        # popular tabela
        self.on_btn_pes_usu_pressed()

        # conectar botões
        self.btnSal_usu.clicked.connect(self.on_btn_sal_usu_pressed)
        self.btnAtu_usu.clicked.connect(self.on_btn_atu_usu_pressed)
        self.btnDel_usu.clicked.connect(self.on_btn_del_usu_pressed)
        self.btnLim_usu.clicked.connect(self.on_btn_clear_usu_pressed)
        self.btnPesUsu_usu.clicked.connect(self.on_btn_pes_usu_pressed)
        self.txtPesUsu_usu.textChanged.connect(self.on_btn_pes_usu_pressed)

        self.table_user.clicked.connect(self.setar_campos_usu)

        # deixar as tabelas somente leitura
        delegate = ReadOnlyDelegate(self.table_user)
        for i in range(8):
            self.table_user.setItemDelegateForColumn(i, delegate)

        # largura padrao da tabela de usuarios
        self.table_user.setColumnWidth(0, 50)
        self.table_user.setColumnWidth(1, 160)
        self.table_user.setColumnWidth(2, 110)
        self.table_user.setColumnWidth(5, 60)
        self.table_user.setColumnWidth(6, 60)
        self.table_user.setColumnWidth(7, 60)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Adicionar novo usuario
    def on_btn_sal_usu_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'insert into tbusuarios(usuario, fone, login, senha, perfil, hora_in, hora_out) values(?,?,?,?,?,?,?)'
        nome = self.txtNom_usu.text()
        fone = self.txtTel_usu.text()
        login = self.txtLog_usu.text()
        senha = self.txtSen_usu.text()
        hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt(7))
        perfil = self.cbbPer_usu.currentText()
        hora_in = self.timInicio.text()
        hora_out = self.timFim.text()
        try:
            if len(nome.strip()) < 4 or len(fone.strip()) < 14 or len(fone.strip()) < 14:
                QMessageBox.warning(self, 'ERRO!!!', 'Preencha os campos obrigatórios para adicionar novo usuário!')
            elif len(senha.strip()) < 4 or len(login.strip()) < 4:
                QMessageBox.warning(self, 'ERRO!!!', 'Login e senha precisam ter pelo menos 4 caracteres!')
            else:
                cursor.execute(sql, [nome, fone, login, hashed, perfil, hora_in, hora_out])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', 'Usuário ADICIONADO com Sucesso!')
                self.on_btn_pes_usu_pressed()
                self.on_btn_clear_usu_pressed()
                db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # atualizar dados de usuario
    def on_btn_atu_usu_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'update tbusuarios set usuario=?, fone=?, login=?, senha=?, perfil=?, hora_in=?, hora_out=? where id=?'
        sql2 = 'update tbhorarios set profissional=? where profissional=?'
        sql3 = 'update horarios_agendados set funcionario=? where funcionario=?'
        nome = self.txtNom_usu.text()
        old_nome = self.old_nome_usu
        fone = self.txtTel_usu.text()
        login = self.txtLog_usu.text()
        senha = self.txtSen_usu.text()
        hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt(7))
        perfil = self.cbbPer_usu.currentText()
        hora_in = self.timInicio.text()
        hora_out = self.timFim.text()
        id = self.txtID_usu.text()
        try:
            if len(nome.strip()) < 4 or len(fone.strip()) < 14 or len(fone.strip()) < 14:
                QMessageBox.warning(self, 'ERRO!!!', 'Preencha os campos obrigatórios para atualizar usuário!')
            elif len(senha.strip()) < 4 or len(login.strip()) < 4:
                QMessageBox.warning(self, 'ERRO!!!', 'Login e senha precisam ter pelo menos 4 caracteres!')
            else:
                cursor.execute(sql, [nome, fone, login, hashed, perfil, hora_in, hora_out, id])
                if nome != old_nome:
                    cursor.execute(sql2, [nome, old_nome])
                    cursor.execute(sql3, [nome, old_nome])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', 'Usuário ATUALIZADO com Sucesso!')
                self.on_btn_pes_usu_pressed()
                self.on_btn_clear_usu_pressed()
                db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # deletar usuarios do banco de dados
    def on_btn_del_usu_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'delete from tbusuarios where id=?'
        id = self.txtID_usu.text()
        confirm = QMessageBox.question(self, 'REMOVER USUÁRIO?',
                                       f'Tem certeza que quer REMOVER o Usuário ({self.txtNom_usu.text()}) do sistema?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                cursor.execute(sql, [id])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', f'Usuário ({self.txtNom_usu.text()}) EXCLUIDO com Sucesso!')
                self.on_btn_pes_usu_pressed()
                self.on_btn_clear_usu_pressed()
                db.close()
            except Exception as e:
                db.close()
                QMessageBox.warning(self, 'ERRO!!!', str(e))
        else:
            db.close()

    def on_btn_pes_usu_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select id as ID,usuario as Nome,fone as Fone,login as Login,senha as Senha,perfil as Perfil,hora_in as ' \
              'Entrada,hora_out as Saída from tbusuarios where usuario like ? '
        search = '%' + self.txtPesUsu_usu.text() + '%'
        try:
            cursor.execute(sql, [search])
            rs = cursor.fetchall()
            row = 0
            self.table_user.setRowCount(len(rs))
            for r in rs:
                self.table_user.setItem(row, 0, QTableWidgetItem(str(r[0])))
                self.table_user.setItem(row, 1, QTableWidgetItem(r[1]))
                self.table_user.setItem(row, 2, QTableWidgetItem(r[2]))
                self.table_user.setItem(row, 3, QTableWidgetItem(r[3]))
                self.table_user.setItem(row, 4, QTableWidgetItem(r[4]))
                self.table_user.setItem(row, 5, QTableWidgetItem(r[5]))
                self.table_user.setItem(row, 6, QTableWidgetItem(r[6]))
                self.table_user.setItem(row, 7, QTableWidgetItem(r[7]))
                row += 1
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # popular campos do formulário selecionando uma linha da tabela
    def setar_campos_usu(self):
        self.cbbPer_usu.setEnabled(True)
        self.btnSal_usu.setEnabled(False)
        self.btnSal_usu.setStyleSheet(None)
        self.btnAtu_usu.setEnabled(True)
        self.btnDel_usu.setEnabled(True)
        rows = sorted(set(index.row() for index in self.table_user.selectedIndexes()))
        for r in rows:
            db = sqlite3.connect('dbmehsys.db')
            cursor = db.cursor()
            id_clicked = self.table_user.item(r, 0).text()
            sql = 'SELECT u.id, u.usuario, c.current_user FROM tbusuarios as u inner join utils as c on (? = ' \
                  'c.current_user) limit 2'
            cursor.execute(sql, [id_clicked])
            rs = cursor.fetchall()
            if len(rs) >= 1:
                self.cbbPer_usu.setEnabled(False)
                self.btnDel_usu.setEnabled(False)
            self.txtID_usu.setText(self.table_user.item(r, 0).text())
            self.txtNom_usu.setText(self.table_user.item(r, 1).text())
            self.old_nome_usu = self.table_user.item(r, 1).text()
            self.txtTel_usu.setText(self.table_user.item(r, 2).text())
            self.txtLog_usu.setText(self.table_user.item(r, 3).text())
            # self.txtSen_usu.setText(self.table_user.item(r, 4).text())
            self.cbbPer_usu.setCurrentText(self.table_user.item(r, 5).text())
            if self.table_user.item(r, 6).text() != '':
                self.timInicio.setTime(
                    QTime(int(self.table_user.item(r, 6).text()[:2]), int(self.table_user.item(r, 6).text()[3:])))
            else:
                self.timInicio.setTime(QTime(0, 0))
            if self.table_user.item(r, 7).text() != '':
                self.timFim.setTime(
                    QTime(int(self.table_user.item(r, 7).text()[:2]), int(self.table_user.item(r, 7).text()[3:])))
            else:
                self.timFim.setTime(QTime(0, 0))

    def on_btn_clear_usu_pressed(self):
        self.txtID_usu.setText(None)
        self.txtNom_usu.setText(None)
        self.txtTel_usu.setText(None)
        self.cbbPer_usu.setEnabled(True)
        self.cbbPer_usu.setCurrentIndex(0)
        self.txtLog_usu.setText(None)
        self.txtSen_usu.setText(None)
        self.timInicio.setTime(QTime(0, 0))
        self.timFim.setTime(QTime(0, 0))
        self.btnSal_usu.setEnabled(True)
        self.btnSal_usu.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                      "color: rgb(255, 255, 255);")
        self.btnAtu_usu.setEnabled(False)
        self.btnDel_usu.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user = UserWindow()
    user.show()
    app.exec_()
