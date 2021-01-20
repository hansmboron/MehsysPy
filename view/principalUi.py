# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principalUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 600)
        MainWindow.setMinimumSize(QtCore.QSize(750, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(7, 6, 731, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tabHor = QtWidgets.QWidget()
        self.tabHor.setObjectName("tabHor")
        self.line = QtWidgets.QFrame(self.tabHor)
        self.line.setGeometry(QtCore.QRect(20, 210, 681, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.table_hor = QtWidgets.QTableWidget(self.tabHor)
        self.table_hor.setGeometry(QtCore.QRect(20, 280, 681, 211))
        self.table_hor.setObjectName("table_hor")
        self.table_hor.setColumnCount(6)
        self.table_hor.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(5, item)
        self.layoutWidget = QtWidgets.QWidget(self.tabHor)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 681, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtPesCli_hor = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtPesCli_hor.setClearButtonEnabled(True)
        self.txtPesCli_hor.setObjectName("txtPesCli_hor")
        self.verticalLayout.addWidget(self.txtPesCli_hor)
        self.cbbSer_hor = QtWidgets.QComboBox(self.layoutWidget)
        self.cbbSer_hor.setObjectName("cbbSer_hor")
        self.verticalLayout.addWidget(self.cbbSer_hor)
        self.cbbPro_hor = QtWidgets.QComboBox(self.layoutWidget)
        self.cbbPro_hor.setObjectName("cbbPro_hor")
        self.verticalLayout.addWidget(self.cbbPro_hor)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtId_hor = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtId_hor.setEnabled(False)
        self.txtId_hor.setObjectName("txtId_hor")
        self.verticalLayout_2.addWidget(self.txtId_hor)
        self.dat_hor = QtWidgets.QDateEdit(self.layoutWidget)
        self.dat_hor.setObjectName("dat_hor")
        self.verticalLayout_2.addWidget(self.dat_hor)
        self.cbbHor_hor = QtWidgets.QComboBox(self.layoutWidget)
        self.cbbHor_hor.setObjectName("cbbHor_hor")
        self.verticalLayout_2.addWidget(self.cbbHor_hor)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.tabHor)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 155, 681, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAge_hor = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnAge_hor.setStyleSheet("background-color: rgb(150, 0, 150);\n"
"color: rgb(255, 255, 255);")
        self.btnAge_hor.setObjectName("btnAge_hor")
        self.horizontalLayout_2.addWidget(self.btnAge_hor)
        self.btnAtu_hor = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnAtu_hor.setEnabled(False)
        self.btnAtu_hor.setObjectName("btnAtu_hor")
        self.horizontalLayout_2.addWidget(self.btnAtu_hor)
        self.btnExc_hor = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnExc_hor.setEnabled(False)
        self.btnExc_hor.setObjectName("btnExc_hor")
        self.horizontalLayout_2.addWidget(self.btnExc_hor)
        self.BtnImp_hor = QtWidgets.QPushButton(self.layoutWidget1)
        self.BtnImp_hor.setObjectName("BtnImp_hor")
        self.horizontalLayout_2.addWidget(self.BtnImp_hor)
        self.btnLim_hor = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnLim_hor.setObjectName("btnLim_hor")
        self.horizontalLayout_2.addWidget(self.btnLim_hor)
        self.layoutWidget2 = QtWidgets.QWidget(self.tabHor)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 230, 681, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtPesNom_hor = QtWidgets.QLineEdit(self.layoutWidget2)
        self.txtPesNom_hor.setClearButtonEnabled(True)
        self.txtPesNom_hor.setObjectName("txtPesNom_hor")
        self.horizontalLayout_3.addWidget(self.txtPesNom_hor)
        self.btnPesNom_hor = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnPesNom_hor.setObjectName("btnPesNom_hor")
        self.horizontalLayout_3.addWidget(self.btnPesNom_hor)
        self.txtPesDat_hor = QtWidgets.QLineEdit(self.layoutWidget2)
        self.txtPesDat_hor.setClearButtonEnabled(True)
        self.txtPesDat_hor.setObjectName("txtPesDat_hor")
        self.horizontalLayout_3.addWidget(self.txtPesDat_hor)
        self.btnPesDat_hor = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnPesDat_hor.setObjectName("btnPesDat_hor")
        self.horizontalLayout_3.addWidget(self.btnPesDat_hor)
        self.listPesCli_hor = QtWidgets.QListWidget(self.tabHor)
        self.listPesCli_hor.setGeometry(QtCore.QRect(20, 47, 338, 91))
        self.listPesCli_hor.setObjectName("listPesCli_hor")
        self.tabWidget.addTab(self.tabHor, "")
        self.tabCli = QtWidgets.QWidget()
        self.tabCli.setObjectName("tabCli")
        self.layoutWidget3 = QtWidgets.QWidget(self.tabCli)
        self.layoutWidget3.setGeometry(QtCore.QRect(120, 230, 481, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txtPesNom_cli = QtWidgets.QLineEdit(self.layoutWidget3)
        self.txtPesNom_cli.setClearButtonEnabled(True)
        self.txtPesNom_cli.setObjectName("txtPesNom_cli")
        self.horizontalLayout_4.addWidget(self.txtPesNom_cli)
        self.btnPesNom_cli = QtWidgets.QPushButton(self.layoutWidget3)
        self.btnPesNom_cli.setObjectName("btnPesNom_cli")
        self.horizontalLayout_4.addWidget(self.btnPesNom_cli)
        self.table_cli = QtWidgets.QTableWidget(self.tabCli)
        self.table_cli.setGeometry(QtCore.QRect(20, 280, 681, 211))
        self.table_cli.setObjectName("table_cli")
        self.table_cli.setColumnCount(6)
        self.table_cli.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(5, item)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabCli)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 155, 681, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnSal_cli = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnSal_cli.setStyleSheet("background-color: rgb(0, 150, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnSal_cli.setObjectName("btnSal_cli")
        self.horizontalLayout_5.addWidget(self.btnSal_cli)
        self.btnAtu_cli = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnAtu_cli.setEnabled(False)
        self.btnAtu_cli.setObjectName("btnAtu_cli")
        self.horizontalLayout_5.addWidget(self.btnAtu_cli)
        self.btnExc_cli = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnExc_cli.setEnabled(False)
        self.btnExc_cli.setObjectName("btnExc_cli")
        self.horizontalLayout_5.addWidget(self.btnExc_cli)
        self.btnLim_cli = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnLim_cli.setObjectName("btnLim_cli")
        self.horizontalLayout_5.addWidget(self.btnLim_cli)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tabCli)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 10, 681, 141))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txtNom_cli = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.txtNom_cli.setClearButtonEnabled(True)
        self.txtNom_cli.setObjectName("txtNom_cli")
        self.verticalLayout_3.addWidget(self.txtNom_cli)
        self.cbcSex_cli = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cbcSex_cli.setObjectName("cbcSex_cli")
        self.verticalLayout_3.addWidget(self.cbcSex_cli)
        self.txtCpf_cli = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.txtCpf_cli.setClearButtonEnabled(True)
        self.txtCpf_cli.setObjectName("txtCpf_cli")
        self.verticalLayout_3.addWidget(self.txtCpf_cli)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txtId_cli = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.txtId_cli.setEnabled(False)
        self.txtId_cli.setObjectName("txtId_cli")
        self.verticalLayout_4.addWidget(self.txtId_cli)
        self.txtEnd_cli = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.txtEnd_cli.setObjectName("txtEnd_cli")
        self.verticalLayout_4.addWidget(self.txtEnd_cli)
        self.txtFon_cli = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.txtFon_cli.setObjectName("txtFon_cli")
        self.verticalLayout_4.addWidget(self.txtFon_cli)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.tabCli)
        self.line_2.setGeometry(QtCore.QRect(20, 210, 681, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tabCli, "")
        self.tabSer = QtWidgets.QWidget()
        self.tabSer.setObjectName("tabSer")
        self.layoutWidget_4 = QtWidgets.QWidget(self.tabSer)
        self.layoutWidget_4.setGeometry(QtCore.QRect(120, 230, 481, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_9.setClearButtonEnabled(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_7.addWidget(self.lineEdit_9)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_7.addWidget(self.pushButton_15)
        self.table_ser = QtWidgets.QTableWidget(self.tabSer)
        self.table_ser.setGeometry(QtCore.QRect(20, 280, 681, 211))
        self.table_ser.setObjectName("table_ser")
        self.table_ser.setColumnCount(5)
        self.table_ser.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(4, item)
        self.layoutWidget_5 = QtWidgets.QWidget(self.tabSer)
        self.layoutWidget_5.setGeometry(QtCore.QRect(20, 155, 681, 51))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_17.setStyleSheet("background-color: rgb(0, 0, 150);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_8.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_18.setEnabled(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_8.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_19.setEnabled(False)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_8.addWidget(self.pushButton_19)
        self.pushButton_21 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_8.addWidget(self.pushButton_21)
        self.layoutWidget_6 = QtWidgets.QWidget(self.tabSer)
        self.layoutWidget_6.setGeometry(QtCore.QRect(20, 10, 681, 141))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.txtNom_ser = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.txtNom_ser.setClearButtonEnabled(True)
        self.txtNom_ser.setObjectName("txtNom_ser")
        self.verticalLayout_5.addWidget(self.txtNom_ser)
        self.cbbPro_ser = QtWidgets.QComboBox(self.layoutWidget_6)
        self.cbbPro_ser.setObjectName("cbbPro_ser")
        self.verticalLayout_5.addWidget(self.cbbPro_ser)
        self.txtSer_ser = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.txtSer_ser.setClearButtonEnabled(True)
        self.txtSer_ser.setObjectName("txtSer_ser")
        self.verticalLayout_5.addWidget(self.txtSer_ser)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.txtId_ser = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.txtId_ser.setEnabled(False)
        self.txtId_ser.setObjectName("txtId_ser")
        self.verticalLayout_6.addWidget(self.txtId_ser)
        self.horHor_ser = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.horHor_ser.setObjectName("horHor_ser")
        self.verticalLayout_6.addWidget(self.horHor_ser)
        spacerItem = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.tabSer)
        self.line_3.setGeometry(QtCore.QRect(20, 210, 681, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tabWidget.addTab(self.tabSer, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 28))
        self.menubar.setObjectName("menubar")
        self.menuAtendimentos = QtWidgets.QMenu(self.menubar)
        self.menuAtendimentos.setObjectName("menuAtendimentos")
        self.menuClientes = QtWidgets.QMenu(self.menubar)
        self.menuClientes.setObjectName("menuClientes")
        self.menuHor_rios = QtWidgets.QMenu(self.menubar)
        self.menuHor_rios.setObjectName("menuHor_rios")
        self.menuServi_os = QtWidgets.QMenu(self.menubar)
        self.menuServi_os.setObjectName("menuServi_os")
        self.menuSair = QtWidgets.QMenu(self.menubar)
        self.menuSair.setObjectName("menuSair")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClientes = QtWidgets.QAction(MainWindow)
        self.actionClientes.setObjectName("actionClientes")
        self.actionHor_rios = QtWidgets.QAction(MainWindow)
        self.actionHor_rios.setObjectName("actionHor_rios")
        self.actionServi_os = QtWidgets.QAction(MainWindow)
        self.actionServi_os.setObjectName("actionServi_os")
        self.actionUsu_rios = QtWidgets.QAction(MainWindow)
        self.actionUsu_rios.setObjectName("actionUsu_rios")
        self.actionClientes_2 = QtWidgets.QAction(MainWindow)
        self.actionClientes_2.setObjectName("actionClientes_2")
        self.actionHor_rios_2 = QtWidgets.QAction(MainWindow)
        self.actionHor_rios_2.setObjectName("actionHor_rios_2")
        self.actionServi_os_2 = QtWidgets.QAction(MainWindow)
        self.actionServi_os_2.setObjectName("actionServi_os_2")
        self.actionAjuda = QtWidgets.QAction(MainWindow)
        self.actionAjuda.setObjectName("actionAjuda")
        self.actionAddHor = QtWidgets.QAction(MainWindow)
        self.actionAddHor.setObjectName("actionAddHor")
        self.actionSair_2 = QtWidgets.QAction(MainWindow)
        self.actionSair_2.setObjectName("actionSair_2")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.menuAtendimentos.addAction(self.actionHor_rios)
        self.menuAtendimentos.addAction(self.actionClientes)
        self.menuAtendimentos.addAction(self.actionServi_os)
        self.menuClientes.addAction(self.actionUsu_rios)
        self.menuHor_rios.addAction(self.actionHor_rios_2)
        self.menuHor_rios.addAction(self.actionClientes_2)
        self.menuHor_rios.addAction(self.actionServi_os_2)
        self.menuServi_os.addAction(self.actionAjuda)
        self.menuServi_os.addAction(self.actionAddHor)
        self.menuServi_os.addAction(self.actionSobre)
        self.menuSair.addAction(self.actionSair_2)
        self.menubar.addAction(self.menuAtendimentos.menuAction())
        self.menubar.addAction(self.menuClientes.menuAction())
        self.menubar.addAction(self.menuHor_rios.menuAction())
        self.menubar.addAction(self.menuServi_os.menuAction())
        self.menubar.addAction(self.menuSair.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela Principal - Mehsys"))
        self.table_hor.setStatusTip(_translate("MainWindow", "Selecione algum agendamento para atualizar ou deletar"))
        item = self.table_hor.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.table_hor.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.table_hor.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Serviço"))
        item = self.table_hor.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data"))
        item = self.table_hor.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Horário"))
        item = self.table_hor.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Profissional"))
        self.txtPesCli_hor.setStatusTip(_translate("MainWindow", "Digite qualquer coisa para pesquisar um cliente"))
        self.txtPesCli_hor.setPlaceholderText(_translate("MainWindow", "Pesquisar cliente"))
        self.cbbSer_hor.setStatusTip(_translate("MainWindow", "Selecione um serviço"))
        self.cbbSer_hor.setPlaceholderText(_translate("MainWindow", "Selecionar serviço"))
        self.cbbPro_hor.setStatusTip(_translate("MainWindow", "Selecione um profissional"))
        self.cbbPro_hor.setPlaceholderText(_translate("MainWindow", "Selecionar Profissional"))
        self.txtId_hor.setStatusTip(_translate("MainWindow", "Código do agendamento"))
        self.txtId_hor.setPlaceholderText(_translate("MainWindow", "Id"))
        self.dat_hor.setStatusTip(_translate("MainWindow", "Digite data para o agendamento"))
        self.cbbHor_hor.setStatusTip(_translate("MainWindow", "Selecione horário disponível(se não aparecer nada clique fora ou no botão \'Agendar\')"))
        self.cbbHor_hor.setPlaceholderText(_translate("MainWindow", "Selecionar horário"))
        self.btnAge_hor.setStatusTip(_translate("MainWindow", "Criar novo agendamento"))
        self.btnAge_hor.setText(_translate("MainWindow", "Agendar"))
        self.btnAtu_hor.setStatusTip(_translate("MainWindow", "Atualizar agendameto"))
        self.btnAtu_hor.setText(_translate("MainWindow", "Atualizar"))
        self.btnExc_hor.setStatusTip(_translate("MainWindow", "Deletar agendamento"))
        self.btnExc_hor.setText(_translate("MainWindow", "Excluir"))
        self.BtnImp_hor.setStatusTip(_translate("MainWindow", "Imprimir comprovante"))
        self.BtnImp_hor.setText(_translate("MainWindow", "Imprimir"))
        self.btnLim_hor.setStatusTip(_translate("MainWindow", "Limpar campos para poder realizar novo agendamento"))
        self.btnLim_hor.setText(_translate("MainWindow", "Limpar"))
        self.txtPesNom_hor.setStatusTip(_translate("MainWindow", "Pesquisar agendamentos por nome do cliente"))
        self.txtPesNom_hor.setPlaceholderText(_translate("MainWindow", "Nome cliente"))
        self.btnPesNom_hor.setStatusTip(_translate("MainWindow", "Pesquisar agendamentos por nome de cliente"))
        self.btnPesNom_hor.setText(_translate("MainWindow", "Pesquisar"))
        self.txtPesDat_hor.setStatusTip(_translate("MainWindow", "pesquisar agendamento por data"))
        self.txtPesDat_hor.setPlaceholderText(_translate("MainWindow", "Data agendamento"))
        self.btnPesDat_hor.setStatusTip(_translate("MainWindow", "Pesquisar agendamento por data"))
        self.btnPesDat_hor.setText(_translate("MainWindow", "Pesquisar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHor), _translate("MainWindow", "Horários"))
        self.txtPesNom_cli.setStatusTip(_translate("MainWindow", "Pesquisar clientes por nome"))
        self.txtPesNom_cli.setPlaceholderText(_translate("MainWindow", "Nome cliente"))
        self.btnPesNom_cli.setStatusTip(_translate("MainWindow", "Pesquisar clientes por nome"))
        self.btnPesNom_cli.setText(_translate("MainWindow", "Pesquisar"))
        self.table_cli.setStatusTip(_translate("MainWindow", "Selecione algum cliente para atualizar ou deletar"))
        item = self.table_cli.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.table_cli.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.table_cli.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sexo"))
        item = self.table_cli.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.table_cli.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Endereço"))
        item = self.table_cli.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fone"))
        self.btnSal_cli.setStatusTip(_translate("MainWindow", "Cadastrar novo cliente"))
        self.btnSal_cli.setText(_translate("MainWindow", "Salvar"))
        self.btnAtu_cli.setStatusTip(_translate("MainWindow", "Atualizar dados do cliente"))
        self.btnAtu_cli.setText(_translate("MainWindow", "Atualizar"))
        self.btnExc_cli.setStatusTip(_translate("MainWindow", "Deletar cliente"))
        self.btnExc_cli.setText(_translate("MainWindow", "Excluir"))
        self.btnLim_cli.setStatusTip(_translate("MainWindow", "Limpar campos para poder cadastrar novo cliente"))
        self.btnLim_cli.setText(_translate("MainWindow", "Limpar"))
        self.txtNom_cli.setStatusTip(_translate("MainWindow", "Digite nome do cliente"))
        self.txtNom_cli.setPlaceholderText(_translate("MainWindow", "Nome cliente"))
        self.cbcSex_cli.setStatusTip(_translate("MainWindow", "Selecione sexo do cliente"))
        self.cbcSex_cli.setPlaceholderText(_translate("MainWindow", "Selecionar sexo"))
        self.txtCpf_cli.setStatusTip(_translate("MainWindow", "Digite CPF do cliente"))
        self.txtCpf_cli.setPlaceholderText(_translate("MainWindow", "CPF cliente"))
        self.txtId_cli.setStatusTip(_translate("MainWindow", "Código do cliente"))
        self.txtId_cli.setPlaceholderText(_translate("MainWindow", "Id"))
        self.txtEnd_cli.setStatusTip(_translate("MainWindow", "Endereço do cliente"))
        self.txtEnd_cli.setPlaceholderText(_translate("MainWindow", "Endereço cliente"))
        self.txtFon_cli.setStatusTip(_translate("MainWindow", "Telefone do cliente"))
        self.txtFon_cli.setPlaceholderText(_translate("MainWindow", "Fone cliente"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCli), _translate("MainWindow", "Clientes"))
        self.lineEdit_9.setStatusTip(_translate("MainWindow", "Pesquisar serviço por nome"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "Nome serviço"))
        self.pushButton_15.setStatusTip(_translate("MainWindow", "Pesquisar serviço por nome"))
        self.pushButton_15.setText(_translate("MainWindow", "Pesquisar"))
        self.table_ser.setStatusTip(_translate("MainWindow", "Selecione algum serviço para atualizar ou deletar"))
        item = self.table_ser.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.table_ser.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.table_ser.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Profissional"))
        item = self.table_ser.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.table_ser.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Duração"))
        self.pushButton_17.setStatusTip(_translate("MainWindow", "Cadastrar novo serviço"))
        self.pushButton_17.setText(_translate("MainWindow", "Salvar"))
        self.pushButton_18.setStatusTip(_translate("MainWindow", "Atualizar serviço"))
        self.pushButton_18.setText(_translate("MainWindow", "Atualizar"))
        self.pushButton_19.setStatusTip(_translate("MainWindow", "Deletar serviço"))
        self.pushButton_19.setText(_translate("MainWindow", "Excluir"))
        self.pushButton_21.setStatusTip(_translate("MainWindow", "Limpar campos para poder adicionar novo serviço"))
        self.pushButton_21.setText(_translate("MainWindow", "Limpar"))
        self.txtNom_ser.setStatusTip(_translate("MainWindow", "Digite nome do serviço"))
        self.txtNom_ser.setPlaceholderText(_translate("MainWindow", "Nome serviço"))
        self.cbbPro_ser.setStatusTip(_translate("MainWindow", "Selecione profissional que realizará este serviço"))
        self.cbbPro_ser.setPlaceholderText(_translate("MainWindow", "Selecionar profissional"))
        self.txtSer_ser.setStatusTip(_translate("MainWindow", "Digite valor do serviço"))
        self.txtSer_ser.setPlaceholderText(_translate("MainWindow", "Valor serviço"))
        self.txtId_ser.setStatusTip(_translate("MainWindow", "Código do serviço"))
        self.txtId_ser.setPlaceholderText(_translate("MainWindow", "Id"))
        self.horHor_ser.setStatusTip(_translate("MainWindow", "Digite duração aproximada do serviço"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSer), _translate("MainWindow", "Serviços"))
        self.menuAtendimentos.setTitle(_translate("MainWindow", "Atendimentos"))
        self.menuClientes.setTitle(_translate("MainWindow", "Usuários"))
        self.menuHor_rios.setTitle(_translate("MainWindow", "Relatórios"))
        self.menuServi_os.setTitle(_translate("MainWindow", "Opções"))
        self.menuSair.setTitle(_translate("MainWindow", "Sair"))
        self.actionClientes.setText(_translate("MainWindow", "Clientes"))
        self.actionClientes.setShortcut(_translate("MainWindow", "Alt+2"))
        self.actionHor_rios.setText(_translate("MainWindow", "Horários"))
        self.actionHor_rios.setShortcut(_translate("MainWindow", "Alt+1"))
        self.actionServi_os.setText(_translate("MainWindow", "Serviços"))
        self.actionServi_os.setShortcut(_translate("MainWindow", "Alt+3"))
        self.actionUsu_rios.setText(_translate("MainWindow", "Usuários"))
        self.actionUsu_rios.setShortcut(_translate("MainWindow", "Alt+4"))
        self.actionClientes_2.setText(_translate("MainWindow", "Clientes"))
        self.actionClientes_2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionHor_rios_2.setText(_translate("MainWindow", "Horários"))
        self.actionHor_rios_2.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionServi_os_2.setText(_translate("MainWindow", "Serviços"))
        self.actionServi_os_2.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionAjuda.setText(_translate("MainWindow", "Ajuda"))
        self.actionAjuda.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionAddHor.setText(_translate("MainWindow", "Adicionar horários"))
        self.actionSair_2.setText(_translate("MainWindow", "Sair"))
        self.actionSair_2.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        self.actionSobre.setShortcut(_translate("MainWindow", "Ctrl+I"))
