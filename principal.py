import sqlite3
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QMainWindow, QDesktopWidget, QFileDialog, QMenu
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors

from Utils.readOnly import ReadOnlyDelegate
from usuario import UserWindow
from view.principalUi import Ui_MainWindow
from trabalho import TrabalhoWindow
from sobre import SobreWindow
from Utils.validaCPF import Valida


class PrincipalWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # centralizar tela
        self.center()
        # add input Masks
        self.txtCpf_cli.setInputMask('###.###.###-##')
        self.txtFon_cli.setInputMask('(##) #####-####')
        self.txtSer_ser.setInputMask('R$#.###,##')
        self.horHor_ser.setInputMask('#:##min')
        self.horHor_ser.setText('n')

        self.centralwidget.installEventFilter(self)

        # largura padrao das tabelas
        self.table_hor.setColumnWidth(0, 50)
        self.table_hor.setColumnWidth(1, 180)
        self.table_hor.setColumnWidth(5, 120)
        self.table_cli.setColumnWidth(0, 50)
        self.table_cli.setColumnWidth(1, 190)
        self.table_ser.setColumnWidth(0, 50)
        self.table_ser.setColumnWidth(1, 200)
        self.table_ser.setColumnWidth(2, 200)

        # deixar as tabelas somente leitura
        delegate = ReadOnlyDelegate(self.table_hor)
        for i in range(6):
            self.table_hor.setItemDelegateForColumn(i, delegate)

        delegate = ReadOnlyDelegate(self.table_cli)
        for i in range(6):
            self.table_cli.setItemDelegateForColumn(i, delegate)

        delegate = ReadOnlyDelegate(self.table_ser)
        for i in range(5):
            self.table_ser.setItemDelegateForColumn(i, delegate)

        # desativar lista de pesquisa de clientes por padrao
        self.listPesCli_hor.setVisible(False)
        # self.listPesCli_hor.setEnabled(False)

        # conectar Métodos com componentes da view
        self.actionSair_2.triggered.connect(self.closeEvent)
        self.actionClientes.triggered.connect(self.on_menu_clientes)
        self.actionHor_rios.triggered.connect(self.on_menu_horarios)
        self.actionServi_os.triggered.connect(self.on_menu_servicos)
        self.actionClientes_2.triggered.connect(self.create_pdf_clients)
        self.actionServi_os_2.triggered.connect(self.create_pdf_services)
        self.actionHor_rios_2.triggered.connect(self.create_pdf_agendamentos)
        self.actionUsu_rios.triggered.connect(self.open_users_screen)
        self.actionAddHor.triggered.connect(self.open_addHor_screen)
        self.actionSobre.triggered.connect(self.open_sobre_screen)
        self.btnSal_cli.clicked.connect(self.on_btn_sal_cli_pressed)
        self.btnAtu_cli.clicked.connect(self.on_btn_atu_cli_pressed)
        self.btnExc_cli.clicked.connect(self.on_btn_del_cli_pressed)
        self.btnLim_cli.clicked.connect(self.on_btn_clear_cli_pressed)
        self.btnPesNom_cli.clicked.connect(self.pesquisar_clientes)
        self.txtPesNom_cli.textChanged.connect(self.pesquisar_clientes)
        self.pushButton_17.clicked.connect(self.on_btn_sal_ser_pressed)
        self.pushButton_18.clicked.connect(self.on_btn_atu_ser_pressed)
        self.pushButton_19.clicked.connect(self.on_btn_del_ser_pressed)
        self.pushButton_21.clicked.connect(self.on_btn_clear_ser_pressed)
        self.pushButton_15.clicked.connect(self.pesquisar_servicos)
        self.lineEdit_9.textChanged.connect(self.pesquisar_servicos)
        self.btnAge_hor.clicked.connect(self.on_btn_sal_hor_pressed)
        self.btnAtu_hor.clicked.connect(self.on_btn_atu_hor_pressed)
        self.btnExc_hor.clicked.connect(self.on_btn_del_hor_pressed)
        self.btnImp_hor.clicked.connect(self.on_btn_imprimir)
        self.btnLim_hor.clicked.connect(self.on_btn_clear_hor_pressed)
        self.btnPesNom_hor.clicked.connect(self.pesquisar_horarios)
        self.txtPesNom_hor.textChanged.connect(self.pesquisar_horarios)
        self.btnPesDat_hor.clicked.connect(self.pesq_hor_by_date)
        self.txtPesDat_hor.textChanged.connect(self.pesq_hor_by_date)
        self.tabWidget.currentChanged.connect(self.popula_todas_tabelas)
        self.txtPesCli_hor.textChanged.connect(self.popula_list_cli)
        self.listPesCli_hor.clicked.connect(self.get_item_selected)

        self.table_cli.clicked.connect(self.setar_campos_cli)
        self.table_ser.clicked.connect(self.setar_campos_ser)
        self.table_hor.clicked.connect(self.setar_campos_hor)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)

    # pergunta para sair do programa
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Sair?", "Tem certeza que quer Sair?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            db = sqlite3.connect('dbmehsys.db')
            cursor = db.cursor()
            sql = 'DELETE FROM utils WHERE current_user;'
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            sys.exit(0)
        else:
            event.ignore()

    def mousePressEvent(self, event):
        if self.cbbPro_hor.currentIndex() < 0:
            self.popula_cbb_profissional_hor()
            self.pesquisar_horarios()
        if event.buttons() and self.cbbPro_hor.currentIndex() >= 1 and self.cbbSer_hor.currentIndex() >= 1 and \
                len(
                    self.txtPesCli_hor.text()) >= 4 and self.cbbHor_hor.currentIndex() < 0 and self.dat_hor.text() != '01/01/2000':
            self.popula_cbb_horarios()

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        actHor = menu.addAction("Horários")
        actCli = menu.addAction("Clientes")
        actSer = menu.addAction("Serviços")
        menu.addSeparator()
        actAdd = menu.addAction("Adicionar Horários")
        actSob = menu.addAction("Sobre")
        actSai = menu.addAction("Sair")

        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == actHor:
            self.on_menu_horarios()
        elif action == actCli:
            self.on_menu_clientes()
        elif action == actSer:
            self.on_menu_servicos()
        elif action == actAdd:
            self.open_addHor_screen()
        elif action == actSob:
            self.open_sobre_screen()
        elif action == actSai:
            self.closeEvent(event)

    # centralizar tela
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def open_users_screen(self):
        self.cbbPro_hor.setCurrentIndex(0)
        self.user = UserWindow()
        self.user.setWindowModality(Qt.ApplicationModal)
        self.user.show()
        self.cbbPro_hor.clear()

    def open_addHor_screen(self):
        self.cbbHor_hor.clear()
        self.trabalho = TrabalhoWindow()
        self.trabalho.show()

    def open_sobre_screen(self):
        self.sobre = SobreWindow()
        self.sobre.show()

    def on_menu_clientes(self):
        self.tabWidget.setCurrentIndex(1)
        self.pesquisar_clientes()

    def on_menu_horarios(self):
        self.tabWidget.setCurrentIndex(0)
        self.pesquisar_horarios()

    def on_menu_servicos(self):
        self.tabWidget.setCurrentIndex(2)
        self.pesquisar_servicos()

    def popula_todas_tabelas(self):
        self.pesquisar_horarios()
        self.pesquisar_clientes()
        self.pesquisar_servicos()
        self.popula_cbb_servicos()
        self.popula_cbb_profissional()
        self.popula_cbb_profissional_hor()

    # MÉTODOS TAB CLIENTES --------------------------------------------------------------

    # Adicionar novo cliente
    def on_btn_sal_cli_pressed(self):
        val_cpf = Valida()
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'insert into tbclientes(nome, sexo, cpf, endereco, fone) values(?,?,?,?,?)'
        nome = self.txtNom_cli.text()
        sexo = self.cbcSex_cli.currentText()
        cpf = self.txtCpf_cli.text()
        endereco = self.txtEnd_cli.text()
        fone = self.txtFon_cli.text()
        try:
            if len(nome.strip()) < 4 or len(cpf.strip()) < 14 or len(fone.strip()) < 14:
                QMessageBox.warning(self, 'ERRO!!!', 'Preencha os campos obrigatórios para adicionar novo cliente!')
            elif not val_cpf.validaCPf(cpf):
                QMessageBox.warning(self, 'CPF INVÁLIDO!!!', 'CPF INVÁLIDO!\nVerifique o CPF digitado!')
            else:
                cursor.execute(sql, [nome, sexo, cpf, endereco, fone])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', 'Cliente ADICIONADO com Sucesso!')
                self.pesquisar_clientes()
                self.on_btn_clear_cli_pressed()
                db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # atualizar dados de cliente
    def on_btn_atu_cli_pressed(self):
        val_cpf = Valida()
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'update tbclientes set nome=?, sexo=?, cpf=?, endereco=?, fone=? where id=?'
        sql2 = 'update tbhorarios set cliente=? where cliente=?'  # atualiza o nome também na tabela de agendamentos
        nome = self.txtNom_cli.text()
        old_nome = self.old_nome_cli
        sexo = self.cbcSex_cli.currentText()
        cpf = self.txtCpf_cli.text()
        endereco = self.txtEnd_cli.text()
        fone = self.txtFon_cli.text()
        id = self.txtId_cli.text()
        try:
            if len(nome.strip()) < 4 or len(cpf.strip()) < 14 or len(fone.strip()) < 14:
                QMessageBox.warning(self, 'Preencha os campos', 'Preencha os campos obrigatórios para atualizar dados '
                                                                'do cliente')
            elif not val_cpf.validaCPf(cpf):
                QMessageBox.warning(self, 'CPF INVÁLIDO!!!', 'CPF INVÁLIDO!\nVerifique o CPF digitado!')
            else:
                cursor.execute(sql, [nome, sexo, cpf, endereco, fone, id])
                if nome != old_nome:
                    cursor.execute(sql2, [nome, old_nome])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', 'Cliente ATUALIZADO com Sucesso!')
                self.pesquisar_clientes()
                self.on_btn_clear_cli_pressed()
                db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # deletar cliente do banco de dados
    def on_btn_del_cli_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'delete from tbclientes where id=?'
        id = self.txtId_cli.text()
        confirm = QMessageBox.question(self, 'REMOVER CLIENTE?',
                                       f'Tem certeza que quer REMOVER o cliente ({self.txtNom_cli.text()})?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                cursor.execute(sql, [id])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', f'Cliente ({self.txtNom_cli.text()}) EXCLUIDO com Sucesso!')
                self.pesquisar_clientes()
                self.on_btn_clear_cli_pressed()
                db.close()
            except Exception as e:
                db.close()
                QMessageBox.warning(self, 'ERRO!!!', str(e))
        else:
            db.close()

    def on_btn_clear_cli_pressed(self):
        self.txtId_cli.setText(None)
        self.txtNom_cli.setText(None)
        self.cbcSex_cli.setCurrentIndex(0)
        self.txtCpf_cli.setText(None)
        self.txtEnd_cli.setText(None)
        self.txtFon_cli.setText(None)
        self.btnSal_cli.setEnabled(True)
        self.btnSal_cli.setStyleSheet("color: #fff;\n"
                                      "background-color: rgb(0, 170, 0);\n")
        self.btnAtu_cli.setEnabled(False)
        self.btnExc_cli.setEnabled(False)

    # Carregar tabela com dados dos clientes
    def pesquisar_clientes(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select id as ID, nome as Nome, sexo as Sexo, cpf as CPF, endereco as Ender, fone as Fone from ' \
              'tbclientes where nome like ? '
        search = '%' + self.txtPesNom_cli.text() + '%'
        cursor.execute(sql, [search])
        rs = cursor.fetchall()
        row = 0
        self.table_cli.setRowCount(len(rs))
        for r in rs:
            self.table_cli.setItem(row, 0, QTableWidgetItem(str(r[0])))
            self.table_cli.setItem(row, 1, QTableWidgetItem(r[1]))
            self.table_cli.setItem(row, 2, QTableWidgetItem(r[2]))
            self.table_cli.setItem(row, 3, QTableWidgetItem(r[3]))
            self.table_cli.setItem(row, 4, QTableWidgetItem(r[4]))
            self.table_cli.setItem(row, 5, QTableWidgetItem(r[5]))
            row += 1
        db.close()

    # popular campos do formulário selecionando uma linha da tabela
    def setar_campos_cli(self):
        rows = sorted(set(index.row() for index in self.table_cli.selectedIndexes()))
        for r in rows:
            self.txtId_cli.setText(self.table_cli.item(r, 0).text())
            self.old_nome_cli = self.table_cli.item(r, 1).text()
            self.txtNom_cli.setText(self.table_cli.item(r, 1).text())
            self.cbcSex_cli.setCurrentText(self.table_cli.item(r, 2).text())
            self.txtCpf_cli.setText(self.table_cli.item(r, 3).text())
            self.txtEnd_cli.setText(self.table_cli.item(r, 4).text())
            self.txtFon_cli.setText(self.table_cli.item(r, 5).text())
        self.btnSal_cli.setEnabled(False)
        self.btnSal_cli.setStyleSheet(None)
        self.btnAtu_cli.setEnabled(True)
        self.btnExc_cli.setEnabled(True)

    def create_pdf_clients(self):
        confirm = QMessageBox.question(self, 'CONFIRMA IMPRESSÃO?',
                                       'Confirma a impressão de um arquivo em "pdf" contendo\ntodos os clientes '
                                       'cadastrados no bando de dados?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            file = QFileDialog.getSaveFileName(self, 'Salvar Arquivo', 'clientes.pdf')
            if file[0]:
                try:
                    doc = SimpleDocTemplate(file[0], title='Relatório de Clientes')
                    flow_obj = []
                    td = [["ID", "NOME", "SEXO", "CPF", "ENDEREÇO", "TELEFONE"]]
                    db = sqlite3.connect('dbmehsys.db')
                    cursor = db.cursor()
                    cursor.execute("select * from tbclientes order by nome")
                    rs = cursor.fetchall()
                    for i in range(len(rs)):
                        data = [rs[i][0], rs[i][1], rs[i][2], rs[i][3], rs[i][4], rs[i][5]]
                        td.append(data)
                    styleSheet = getSampleStyleSheet()
                    style = styleSheet['Title']
                    title = Paragraph("Relatório de Clientes", style)
                    table = Table(td)
                    db.close()
                    ts = TableStyle([("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                                     ("BACKGROUND", (0, 0), (-1, 0), colors.mediumpurple),
                                     ("BACKGROUND", (0, 1), (-1, -1), colors.lightseagreen)])
                    table.setStyle(ts)
                    flow_obj.append(title)
                    flow_obj.append(table)
                    doc.build(flow_obj)
                    QMessageBox.information(
                        self, 'Relatório gerado com SUCESSO!!!', f'Relatório de Clientes salvo em: "{file[0]}"')
                except Exception as e:
                    QMessageBox.warning(self, 'ERRO!!!', str(e))

    # METODOS TAB SERVIÇOS ========================================================================

    # Adicionar novo serviço
    def on_btn_sal_ser_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'insert into tbservicos(nome, usuario, valor, duracao) values(?,?,?,?)'
        nome = self.txtNom_ser.text()
        prof = self.cbbPro_ser.currentText()
        valor = self.txtSer_ser.text()
        duracao = self.horHor_ser.text()
        try:
            if len(nome.strip()) < 4 or len(valor.strip()) < 10 or (int(valor[4:7]) <= 0 and int(valor[2:3]) <= 0):
                QMessageBox.warning(self, 'ERRO!!!', 'Preencha os campos obrigatórios para adicionar novo serviço!')
            else:
                cursor.execute(sql, [nome, prof, valor, duracao])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', 'Serviço ADICIONADO com Sucesso!')
                self.pesquisar_servicos()
                self.on_btn_clear_ser_pressed()
                db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # atualizar dados de serviço
    def on_btn_atu_ser_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'update tbservicos set nome=?, usuario=?, valor=?, duracao=? where id=?'
        sql2 = 'update tbhorarios set servico=? where servico=?'
        nome = self.txtNom_ser.text()
        old_nome = self.old_nome_ser
        print(f'Old_nome: {old_nome}')
        prof = self.cbbPro_ser.currentText()
        valor = self.txtSer_ser.text()
        duracao = self.horHor_ser.text()
        id = self.txtId_ser.text()
        try:
            if len(nome.strip()) < 4 or len(valor.strip()) < 10 or (int(valor[4:7]) <= 0 and int(valor[2:3]) <= 0):
                QMessageBox.warning(self, 'Preencha os campos',
                                    'Preencha os campos obrigatórios para atualizar dados '
                                    'do serviço')
            else:
                cursor.execute(sql, [nome, prof, valor, duracao, id])
                if nome != old_nome:
                    cursor.execute(sql2, [nome, old_nome])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', 'Serviço ATUALIZADO com Sucesso!')
                self.pesquisar_servicos()
                self.on_btn_clear_ser_pressed()
                db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # deletar serviço do banco de dados
    def on_btn_del_ser_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'delete from tbservicos where id=?'
        id = self.txtId_ser.text()
        confirm = QMessageBox.question(self, 'REMOVER SERVIÇO?',
                                       f'Tem certeza que quer REMOVER o serviço ({self.txtNom_ser.text()})?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                cursor.execute(sql, [id])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', f'Serviço ({self.txtNom_ser.text()}) EXCLUIDO com Sucesso!')
                self.pesquisar_servicos()
                self.on_btn_clear_ser_pressed()
                db.close()
            except Exception as e:
                db.close()
                QMessageBox.warning(self, 'ERRO!!!', str(e))
        else:
            db.close()

    def on_btn_clear_ser_pressed(self):
        self.txtId_ser.setText(None)
        self.txtNom_ser.setText(None)
        self.cbbPro_ser.setCurrentIndex(0)
        self.txtSer_ser.setText(None)
        self.horHor_ser.setText(None)
        self.pushButton_17.setEnabled(True)
        self.pushButton_17.setStyleSheet("color: #fff;\n"
                                      "background-color: rgb(20, 0, 170);\n")
        self.pushButton_18.setEnabled(False)
        self.pushButton_19.setEnabled(False)

    # Carregar tabela com dados dos serviços
    def pesquisar_servicos(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select id as ID, nome as Nome, usuario as Profissional, valor as Valor, duracao as Duração from ' \
              'tbservicos where nome like ? '
        search = '%' + self.lineEdit_9.text() + '%'
        try:
            cursor.execute(sql, [search])
            rs = cursor.fetchall()
            row = 0
            self.table_ser.setRowCount(len(rs))
            for r in rs:
                self.table_ser.setItem(row, 0, QTableWidgetItem(str(r[0])))
                self.table_ser.setItem(row, 1, QTableWidgetItem(r[1]))
                self.table_ser.setItem(row, 2, QTableWidgetItem(r[2]))
                self.table_ser.setItem(row, 3, QTableWidgetItem(r[3]))
                self.table_ser.setItem(row, 4, QTableWidgetItem(r[4]))
                row += 1
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # popular campos do formulário selecionando uma linha da tabela
    def setar_campos_ser(self):
        rows = sorted(set(index.row() for index in self.table_ser.selectedIndexes()))
        for r in rows:
            self.txtId_ser.setText(self.table_ser.item(r, 0).text())
            self.old_nome_ser = self.table_ser.item(r, 1).text()
            self.txtNom_ser.setText(self.table_ser.item(r, 1).text())
            self.cbbPro_ser.setCurrentText(self.table_ser.item(r, 2).text())
            self.txtSer_ser.setText(self.table_ser.item(r, 3).text())
            self.horHor_ser.setText(self.table_ser.item(r, 4).text())
        self.pushButton_17.setEnabled(False)
        self.pushButton_17.setStyleSheet(None)
        self.pushButton_18.setEnabled(True)
        self.pushButton_19.setEnabled(True)

    # popula combobox profissional
    def popula_cbb_profissional(self):
        self.cbbPro_ser.clear()
        self.cbbPro_ser.addItem("Selecionar")
        self.cbbPro_ser.setCurrentIndex(0)
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select usuario from tbusuarios order by usuario'
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
            for i in range(len(rs)):
                self.cbbPro_ser.addItem(rs[i][0])
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    def create_pdf_services(self):
        confirm = QMessageBox.question(self, 'CONFIRMA IMPRESSÃO?',
                                       'Confirma a impressão de um arquivo em "pdf" contendo\ntodos os serviços '
                                       'cadastrados no bando de dados?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            file = QFileDialog.getSaveFileName(self, 'Salvar Arquivo', 'serviços.pdf')
            if file[0]:
                try:
                    doc = SimpleDocTemplate(file[0], title='Relatório de Serviços')
                    flow_obj = []
                    td = [["ID", "SERVIÇO", "PROFISSIONAL", "VALOR", "DURAÇÃO"]]
                    db = sqlite3.connect('dbmehsys.db')
                    cursor = db.cursor()
                    cursor.execute("select * from tbservicos order by nome")
                    rs = cursor.fetchall()
                    for i in range(len(rs)):
                        data = [rs[i][0], rs[i][1], rs[i][2], rs[i][3], rs[i][4]]
                        td.append(data)
                    styleSheet = getSampleStyleSheet()
                    style = styleSheet['Title']
                    title = Paragraph("Relatório de Serviços", style)
                    table = Table(td)
                    db.close()
                    ts = TableStyle([("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                                     ("BACKGROUND", (0, 0), (-1, 0), colors.mediumpurple),
                                     ("BACKGROUND", (0, 1), (-1, -1), colors.lightskyblue)])
                    table.setStyle(ts)
                    flow_obj.append(title)
                    flow_obj.append(table)
                    doc.build(flow_obj)
                    QMessageBox.information(
                        self, 'Relatório gerado com SUCESSO!!!', f'Relatório de Serviços salvo em: "{file[0]}"')
                except Exception as e:
                    QMessageBox.warning(self, 'ERRO!!!', str(e))

    # METODOS TAB HORÁRIOS =======================================================================

    # Adicionar novo agendamento
    def on_btn_sal_hor_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'insert into tbhorarios(cliente, servico, data, horario, profissional, id_ser) values(?,?,?,?,?,?)'
        sql2 = 'insert into horarios_agendados(data, funcionario, horario) values(?,?,?)'
        cliente = self.txtPesCli_hor.text()
        servico = self.cbbSer_hor.currentText()
        data = self.dat_hor.text()
        horario = self.cbbHor_hor.currentText()
        prof = self.cbbPro_hor.currentText()
        sql3 = 'select nome from tbservicos where nome = ?'
        try:
            cursor.execute(sql3, [servico])
            rs_ser = cursor.fetchall()
            id_ser = -1
            if len(rs_ser) >= 1:
                id_ser = rs_ser[0][0]

            if self.cbbPro_hor.currentIndex() >= 1 and self.cbbSer_hor.currentIndex() >= 1 and \
                    len(
                        self.txtPesCli_hor.text()) >= 4 and self.cbbHor_hor.currentIndex() < 0 and self.dat_hor.text() != '01/01/2000':
                self.popula_cbb_horarios()
                QMessageBox.warning(self, 'ATENÇÃO!!!', 'Selecione o horário disponível na caixa de horários!')

            elif len(
                    cliente.strip()) < 4 or self.cbbHor_hor.currentIndex() <= 0 or self.cbbSer_hor.currentIndex() <= 0 or self.cbbPro_hor.currentIndex() <= 0 or data == '01/01/2000':
                QMessageBox.warning(self, 'ERRO!!!', 'Preencha os campos obrigatórios para criar novo Agendamento!')
            else:
                cursor.execute(sql, [cliente, servico, data, horario, prof, id_ser])
                cursor.execute(sql2, [data, prof, horario])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', 'Agendamento ADICIONADO com Sucesso!')
                self.pesquisar_horarios()
                self.on_btn_clear_hor_pressed()
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # atualizar dados do agendamento
    def on_btn_atu_hor_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'update tbhorarios set cliente=?, servico=?, data=?, horario=?, profissional=?, id_ser=? where id=?'
        sql2 = 'update horarios_agendados set data=?, funcionario=?, horario=? where data=? and funcionario=? and ' \
               'horario=? '
        cliente = self.txtPesCli_hor.text()
        servico = self.cbbSer_hor.currentText()
        data = self.dat_hor.text()
        old_data = self.old_data_hor
        horario = self.cbbHor_hor.currentText()
        old_hor = self.old_horario_hor
        prof = self.cbbPro_hor.currentText()
        old_prof = self.old_prof_hor
        id = self.txtId_hor.text()
        sql3 = 'select nome from tbservicos where nome = ?'
        print(f'NOVOS: {data}  {horario}  {prof}')
        print(f'VELHOS: {old_data}  {old_hor}  {old_prof}')
        try:
            cursor.execute(sql3, [servico])
            rs_ser = cursor.fetchall()
            id_ser = -1
            if len(rs_ser) >= 1:
                id_ser = rs_ser[0][0]

            if self.cbbPro_hor.currentIndex() >= 1 and self.cbbSer_hor.currentIndex() >= 1 and \
                    len(
                        self.txtPesCli_hor.text()) >= 4 and self.cbbHor_hor.currentIndex() < 0 and self.dat_hor.text() != '01/01/2000':
                self.popula_cbb_horarios()
                QMessageBox.warning(self, 'ATENÇÃO!!!', 'Selecione o horário disponível na caixa de horários!')

            elif len(
                    cliente.strip()) < 4 or self.cbbHor_hor.currentIndex() == 0 or self.cbbSer_hor.currentIndex() <= 0 or self.cbbPro_hor.currentIndex() <= 0 or data == '01/01/2000':
                QMessageBox.warning(self, 'ERRO!!!',
                                    'Preencha os campos obrigatórios para Atualizar o Agendamento!')
            else:
                cursor.execute(sql, [cliente, servico, data, horario, prof, id_ser, id])
                cursor.execute(sql2, [data, prof, horario, old_data, old_prof, old_hor])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', 'Agendamento ATUALIZADO com Sucesso!')
                self.pesquisar_horarios()
                self.on_btn_clear_hor_pressed()
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # deletar agendamento do banco de dados
    def on_btn_del_hor_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'delete from tbhorarios where id=?'
        sql2 = 'delete from horarios_agendados where data=? and funcionario=? and horario=?'
        id = self.txtId_hor.text()
        old_data = self.old_data_hor
        old_horario = self.old_horario_hor
        old_prof = self.old_prof_hor
        confirm = QMessageBox.question(self, 'REMOVER AGENDAMENTO?',
                                       f'Tem certeza que quer REMOVER o agendamento nº:({id})?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                cursor.execute(sql, [id])
                cursor.execute(sql2, [old_data, old_prof, old_horario])
                db.commit()
                QMessageBox.information(
                    self, 'SUCESSO!!!', f'Agendamento nº:({id}) EXCLUIDO com Sucesso!')
                self.pesquisar_horarios()
                self.on_btn_clear_hor_pressed()
                db.close()
            except Exception as e:
                db.close()
                QMessageBox.warning(self, 'ERRO!!!', str(e))
        else:
            db.close()

    def on_btn_imprimir(self):
        id = self.txtId_hor.text()
        confirm = QMessageBox.question(self, 'CONFIRMA IMPRESSÃO?',
                                       f'Confirma a impressão do comprovante de agendamento nº ({id})?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            file = QFileDialog.getSaveFileName(self, 'Salvar Arquivo', f'comprovante{id}.pdf')
            if file[0]:
                try:
                    flow_obj = []
                    db = sqlite3.connect('dbmehsys.db')
                    cursor = db.cursor()
                    sql = 'select h.id, h.cliente, h.servico, h.data, h.horario, h.profissional, s.valor, s.duracao ' \
                          'from tbhorarios as h inner join tbservicos as s on (s.nome = h.id_ser) where h.id = ? '
                    cursor.execute(sql, [id])
                    rs = cursor.fetchall()
                    doc = SimpleDocTemplate(file[0], title=f"Comprovante número ({str(rs[0][0])})")

                    styleSheet = getSampleStyleSheet()
                    titleStyle = styleSheet['Title']
                    itemStyle = ParagraphStyle(name='Heading2',
                                               fontSize=16,
                                               leading=18,
                                               textColor=colors.darkmagenta,
                                               spaceBefore=12,
                                               spaceAfter=6)
                    title = Paragraph(f"Comprovante de agendamento número {str(rs[0][0])}", titleStyle)
                    cliente = Paragraph(f"Cliente:            {rs[0][1]}", itemStyle)
                    servico = Paragraph(f"Serviço:            {rs[0][2]}", itemStyle)
                    data = Paragraph(f'Data:               {rs[0][3]}', itemStyle)
                    horario = Paragraph(f'Horário:            {rs[0][4]}', itemStyle)
                    prof = Paragraph(f'Profissional:       {rs[0][5]}', itemStyle)
                    valor = Paragraph(f'Valor:              {rs[0][6]}', itemStyle)
                    duracao = Paragraph(f'Duração aproximada: {rs[0][7]}', itemStyle)
                    flow_obj.append(title)
                    flow_obj.append(cliente)
                    flow_obj.append(servico)
                    flow_obj.append(data)
                    flow_obj.append(horario)
                    flow_obj.append(prof)
                    flow_obj.append(valor)
                    flow_obj.append(duracao)
                    doc.build(flow_obj)
                    cursor.close()
                    db.close()
                    QMessageBox.information(
                        self, 'Comprovante gerado com SUCESSO!!!',
                        f'Comprovante de Agendamento nº {id} salvo em: "{file[0]}"')
                except Exception as e:
                    QMessageBox.warning(self, 'ERRO!!!', str(e))

    def on_btn_clear_hor_pressed(self):
        self.txtId_hor.setText(None)
        self.txtPesCli_hor.setText(None)
        self.cbbSer_hor.setCurrentIndex(0)
        self.cbbPro_hor.setCurrentIndex(0)
        self.dat_hor.setDate(QDate(2000, 1, 1))
        self.cbbHor_hor.setCurrentIndex(0)
        self.cbbSer_hor.setEnabled(True)
        self.btnAtu_hor.setEnabled(False)
        self.btnExc_hor.setEnabled(False)
        self.btnImp_hor.setEnabled(False)
        self.btnAge_hor.setEnabled(True)
        self.btnAge_hor.setStyleSheet("color: #fff;\n"
                                      "background-color: #850085;\n")
        self.listPesCli_hor.setVisible(False)
        self.cbbHor_hor.clear()

    # Carregar tabela com dados dos horarios por nome
    def pesquisar_horarios(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select id as ID, cliente as Cliente, servico as Serviço, data as Data, horario as Horário, ' \
              'profissional as Profissional from tbhorarios where cliente like ? '
        search = '%' + self.txtPesNom_hor.text() + '%'
        try:
            cursor.execute(sql, [search])
            rs = cursor.fetchall()
            row = 0
            self.table_hor.setRowCount(len(rs))
            for r in rs:
                self.table_hor.setItem(row, 0, QTableWidgetItem(str(r[0])))
                self.table_hor.setItem(row, 1, QTableWidgetItem(r[1]))
                self.table_hor.setItem(row, 2, QTableWidgetItem(r[2]))
                self.table_hor.setItem(row, 3, QTableWidgetItem(r[3]))
                self.table_hor.setItem(row, 4, QTableWidgetItem(r[4]))
                self.table_hor.setItem(row, 5, QTableWidgetItem(r[5]))
                row += 1
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # Carregar tabela com dados dos horarios por nome
    def pesq_hor_by_date(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select id as ID, cliente as Cliente, servico as Serviço, data as Data, horario as Horário, ' \
              'profissional as Profissional from tbhorarios where data like ? '
        try:
            search = '%' + self.txtPesDat_hor.text() + '%'
            cursor.execute(sql, [search])
            rs = cursor.fetchall()
            row = 0
            self.table_hor.setRowCount(len(rs))
            for r in rs:
                self.table_hor.setItem(row, 0, QTableWidgetItem(str(r[0])))
                self.table_hor.setItem(row, 1, QTableWidgetItem(r[1]))
                self.table_hor.setItem(row, 2, QTableWidgetItem(r[2]))
                self.table_hor.setItem(row, 3, QTableWidgetItem(r[3]))
                self.table_hor.setItem(row, 4, QTableWidgetItem(r[4]))
                self.table_hor.setItem(row, 5, QTableWidgetItem(r[5]))
                row += 1
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # popular campos do formulário selecionando uma linha da tabela
    def setar_campos_hor(self):
        self.pesquisar_horarios()
        self.popula_cbb_profissional_hor()
        rows = sorted(set(index.row() for index in self.table_hor.selectedIndexes()))
        for r in rows:
            self.txtId_hor.setText(self.table_hor.item(r, 0).text())
            self.txtPesCli_hor.setText(self.table_hor.item(r, 1).text())
            self.cbbSer_hor.setCurrentText(self.table_hor.item(r, 2).text())
            y = int(self.table_hor.item(r, 3).text()[6:])
            m = int(self.table_hor.item(r, 3).text()[3:5])
            d = int(self.table_hor.item(r, 3).text()[:2])
            data = QDate(y, m, d)
            self.old_data_hor = self.table_hor.item(r, 3).text()
            self.old_prof_hor = self.table_hor.item(r, 5).text()
            self.old_horario_hor = self.table_hor.item(r, 4).text()
            self.dat_hor.setDate(data)
            self.cbbHor_hor.setCurrentText(self.table_hor.item(r, 4).text())
            self.cbbPro_hor.setCurrentText(self.table_hor.item(r, 5).text())
        self.btnAtu_hor.setEnabled(True)
        self.btnExc_hor.setEnabled(True)
        self.btnImp_hor.setEnabled(True)
        self.btnAge_hor.setEnabled(False)
        self.btnAge_hor.setStyleSheet(None)
        self.cbbSer_hor.setEnabled(False)
        self.listPesCli_hor.setVisible(False)

    # pesquisa clientes para o campo de texto txtPesCli_hor
    def popula_list_cli(self):
        self.listPesCli_hor.clear()
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = "select nome from tbclientes where nome like ? order by nome"
        search = '%' + self.txtPesCli_hor.text() + '%'
        try:
            cursor.execute(sql, [search])
            rs = cursor.fetchmany(6)
            v = 0
            if len(rs) == 1:
                self.listPesCli_hor.addItem(rs[0][0])
                v = 1
            elif len(rs) == 2:
                self.listPesCli_hor.addItem(rs[0][0])
                self.listPesCli_hor.addItem(rs[1][0])
                v = 2
            elif len(rs) == 3:
                self.listPesCli_hor.addItem(rs[0][0])
                self.listPesCli_hor.addItem(rs[1][0])
                self.listPesCli_hor.addItem(rs[2][0])
                v = 3
            elif len(rs) == 4:
                self.listPesCli_hor.addItem(rs[0][0])
                self.listPesCli_hor.addItem(rs[1][0])
                self.listPesCli_hor.addItem(rs[2][0])
                self.listPesCli_hor.addItem(rs[3][0])
                v = 4
            else:
                while len(rs) > 0 and v <= 4:
                    self.listPesCli_hor.addItem(rs[v][0])
                    v += 1
            db.close()

            if v >= 1:
                self.listPesCli_hor.setVisible(True)
            else:
                self.listPesCli_hor.setVisible(False)

        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # obter valor da lista
    def get_item_selected(self):
        self.txtPesCli_hor.setText(self.listPesCli_hor.currentItem().text())
        self.listPesCli_hor.setVisible(False)

    # popula combobox serviçosF
    def popula_cbb_servicos(self):
        self.cbbSer_hor.clear()
        self.cbbSer_hor.addItem("Selecionar")
        self.cbbSer_hor.setCurrentIndex(0)
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select nome from tbservicos order by nome'
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
            for i in range(len(rs)):
                self.cbbSer_hor.addItem(rs[i][0])
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # popula combobox de horários de atendimento
    def popula_cbb_horarios(self):
        self.cbbHor_hor.clear()
        self.cbbHor_hor.addItem("Selecionar")
        self.cbbHor_hor.setCurrentIndex(0)
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = "select p.* from (select '" \
              + self.dat_hor.text() + "' data, '" + self.cbbPro_hor.currentText() + \
              "' funcionario, horario from " \
              "horarios) p left join " \
              "horarios_agendados c on " \
              "p.horario=c.horario and " \
              "p.data=c.data and " \
              "p.funcionario=c.funcionario where " \
              "c.data is null order by p.data"
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
            for i in range(len(rs)):
                self.cbbHor_hor.addItem(rs[i][2])
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # popula combobox profissionais
    def popula_cbb_profissional_hor(self):
        self.cbbPro_hor.clear()
        self.cbbPro_hor.addItem("Selecionar")
        self.cbbPro_hor.setCurrentIndex(0)
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select usuario from tbusuarios order by usuario'
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
            for i in range(len(rs)):
                self.cbbPro_hor.addItem(rs[i][0])
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    def create_pdf_agendamentos(self):
        confirm = QMessageBox.question(self, 'CONFIRMA IMPRESSÃO?',
                                       'Confirma a impressão de um arquivo em "pdf" contendo\ntodos os agendamentos '
                                       'cadastrados no bando de dados?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            file = QFileDialog.getSaveFileName(self, 'Salvar Arquivo', 'agendamendos.pdf')
            if file[0]:
                try:
                    doc = SimpleDocTemplate(file[0], title="Relatório de Agendamentos")
                    flow_obj = []
                    td = [["ID", "CLIENTE", "SERVIÇO", "DATA", "HORÁRIO", "PROFISSIONAL"]]
                    db = sqlite3.connect('dbmehsys.db')
                    cursor = db.cursor()
                    cursor.execute("select * from tbhorarios order by data")
                    rs = cursor.fetchall()
                    for i in range(len(rs)):
                        data = [rs[i][0], rs[i][1], rs[i][2], rs[i][3], rs[i][4], rs[i][5]]
                        td.append(data)
                    styleSheet = getSampleStyleSheet()
                    style = styleSheet['Title']
                    title = Paragraph("Relatório de Agendamentos", style)
                    table = Table(td)
                    db.close()
                    ts = TableStyle([("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                                     ("BACKGROUND", (0, 0), (-1, 0), colors.mediumpurple),
                                     ("BACKGROUND", (0, 1), (-1, -1), colors.lightsteelblue)])
                    table.setStyle(ts)
                    flow_obj.append(title)
                    flow_obj.append(table)
                    doc.build(flow_obj)
                    QMessageBox.information(
                        self, 'Relatório gerado com SUCESSO!!!', f'Relatório de Agendamentos salvo em: "{file[0]}"')
                except Exception as e:
                    QMessageBox.warning(self, 'ERRO!!!', str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    principal = PrincipalWindow()
    principal.show()
    app.exec_()
