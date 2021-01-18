import sqlite3
import sys

from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject, QSize, QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTabWidget, QFrame, QSizePolicy, QSpacerItem, \
    QTableWidgetItem, QMainWindow, QAction, QHBoxLayout, QPushButton, QVBoxLayout, QComboBox, QLineEdit, \
    QMenuBar, QMenu, QStatusBar, QDateEdit, QTableWidget, QDesktopWidget, QListWidget

from Utils.readOnly import ReadOnlyDelegate
from usuario import UiUsuario


class UiMainWindow(QMainWindow):
    def __init__(self):
        super(UiMainWindow, self).__init__()
        self.centralwidget = QWidget()
        UiMainWindow.setObjectName(self, "MainWindow")
        UiMainWindow.resize(self, 750, 600)
        UiMainWindow.setMinimumSize(self, QSize(750, 600))
        self.center()
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabHor = QWidget()
        self.line = QFrame(self.tabHor)
        self.table_hor = QTableWidget(self.tabHor)
        self.layoutWidget = QWidget(self.tabHor)
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.verticalLayout = QVBoxLayout()
        self.txtPesCli_hor = QLineEdit(self.layoutWidget)
        self.cbbSer_hor = QComboBox(self.layoutWidget)
        self.cbbPro_hor = QComboBox(self.layoutWidget)
        self.verticalLayout_2 = QVBoxLayout()
        self.txtId_hor = QLineEdit(self.layoutWidget)
        self.dat_hor = QDateEdit(self.layoutWidget)
        self.cbbHor_hor = QComboBox(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.tabHor)
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.btnAge_hor = QPushButton(self.layoutWidget1)
        self.btnAtu_hor = QPushButton(self.layoutWidget1)
        self.btnExc_hor = QPushButton(self.layoutWidget1)
        self.BtnImp_hor = QPushButton(self.layoutWidget1)
        self.btnLim_hor = QPushButton(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.tabHor)
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.txtPesNom_hor = QLineEdit(self.layoutWidget2)
        self.btnPesNom_hor = QPushButton(self.layoutWidget2)
        self.txtPesDat_hor = QLineEdit(self.layoutWidget2)
        self.btnPesDat_hor = QPushButton(self.layoutWidget2)
        self.tabCli = QWidget()
        self.layoutWidget3 = QWidget(self.tabCli)
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.txtPesNom_cli = QLineEdit(self.layoutWidget3)
        self.btnPesNom_cli = QPushButton(self.layoutWidget3)
        self.table_cli = QTableWidget(self.tabCli)
        self.layoutWidget_2 = QWidget(self.tabCli)
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_2)
        self.btnSal_cli = QPushButton(self.layoutWidget_2)
        self.btnAtu_cli = QPushButton(self.layoutWidget_2)
        self.btnExc_cli = QPushButton(self.layoutWidget_2)
        self.btnLim_cli = QPushButton(self.layoutWidget_2)
        self.layoutWidget_3 = QWidget(self.tabCli)
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3 = QVBoxLayout()
        self.txtNom_cli = QLineEdit(self.layoutWidget_3)
        self.cbcSex_cli = QComboBox(self.layoutWidget_3)
        self.txtCpf_cli = QLineEdit(self.layoutWidget_3)
        self.verticalLayout_4 = QVBoxLayout()
        self.txtId_cli = QLineEdit(self.layoutWidget_3)
        self.txtEnd_cli = QLineEdit(self.layoutWidget_3)
        self.txtFon_cli = QLineEdit(self.layoutWidget_3)
        self.line_2 = QFrame(self.tabCli)
        self.tabSer = QWidget()
        self.layoutWidget_4 = QWidget(self.tabSer)
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_4)
        self.lineEdit_9 = QLineEdit(self.layoutWidget_4)
        self.pushButton_15 = QPushButton(self.layoutWidget_4)
        self.table_ser = QTableWidget(self.tabSer)
        self.layoutWidget_5 = QWidget(self.tabSer)
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_5)
        self.pushButton_17 = QPushButton(self.layoutWidget_5)
        self.pushButton_18 = QPushButton(self.layoutWidget_5)
        self.pushButton_19 = QPushButton(self.layoutWidget_5)
        self.pushButton_21 = QPushButton(self.layoutWidget_5)
        self.layoutWidget_6 = QWidget(self.tabSer)
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_6)
        self.verticalLayout_5 = QVBoxLayout()
        self.txtNom_ser = QLineEdit(self.layoutWidget_6)
        self.cbbPro_ser = QComboBox(self.layoutWidget_6)
        self.txtSer_ser = QLineEdit(self.layoutWidget_6)
        self.verticalLayout_6 = QVBoxLayout()
        self.txtId_ser = QLineEdit(self.layoutWidget_6)
        self.horHor_ser = QLineEdit(self.layoutWidget_6)
        self.line_3 = QFrame(self.tabSer)
        self.menubar = QMenuBar(self)
        self.menuAtendimentos = QMenu(self.menubar)
        self.menuClientes = QMenu(self.menubar)
        self.menuHor_rios = QMenu(self.menubar)
        self.menuServi_os = QMenu(self.menubar)
        self.menuSair = QMenu(self.menubar)
        self.statusbar = QStatusBar()
        self.actionHor_rios = QAction()
        self.actionClientes = QAction()
        self.actionServi_os = QAction()
        self.actionUsu_rios = QAction()
        self.actionUsu_rios.setEnabled(False)
        self.actionClientes_2 = QAction()
        self.actionClientes_2.setEnabled(False)
        self.actionHor_rios_2 = QAction()
        self.actionHor_rios_2.setEnabled(False)
        self.actionServi_os_2 = QAction()
        self.actionServi_os_2.setEnabled(False)
        self.actionAjuda = QAction()
        self.actionAddHor = QAction()
        self.actionAddHor.setEnabled(False)
        self.actionSair_2 = QAction()
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget.setGeometry(QRect(7, 6, 731, 541))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tabHor.setObjectName("tabHor")
        self.line.setGeometry(QRect(20, 210, 681, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.table_hor.setGeometry(QRect(20, 280, 681, 211))
        self.table_hor.setObjectName("table_hor")
        self.table_hor.setColumnCount(6)
        self.table_hor.setRowCount(0)
        delegate = ReadOnlyDelegate(self.table_hor)
        item = QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(0, item)
        self.table_hor.setItemDelegateForColumn(0, delegate)
        item = QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(1, item)
        self.table_hor.setItemDelegateForColumn(1, delegate)
        item = QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(2, item)
        self.table_hor.setItemDelegateForColumn(2, delegate)
        item = QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(3, item)
        self.table_hor.setItemDelegateForColumn(3, delegate)
        item = QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(4, item)
        self.table_hor.setItemDelegateForColumn(4, delegate)
        item = QTableWidgetItem()
        self.table_hor.setHorizontalHeaderItem(5, item)
        self.table_hor.setItemDelegateForColumn(5, delegate)
        self.layoutWidget.setGeometry(QRect(20, 10, 681, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtPesCli_hor.setClearButtonEnabled(True)
        self.txtPesCli_hor.setObjectName("txtPesCli_hor")
        self.verticalLayout.addWidget(self.txtPesCli_hor)
        self.cbbSer_hor.setObjectName("cbbSer_hor")
        self.verticalLayout.addWidget(self.cbbSer_hor)
        self.cbbPro_hor.setObjectName("cbbPro_hor")
        self.verticalLayout.addWidget(self.cbbPro_hor)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtId_hor.setObjectName("txtId_hor")
        self.verticalLayout_2.addWidget(self.txtId_hor)
        self.dat_hor.setObjectName("dat_hor")
        self.verticalLayout_2.addWidget(self.dat_hor)
        self.cbbHor_hor.setObjectName("cbbHor_hor")
        self.verticalLayout_2.addWidget(self.cbbHor_hor)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1.setGeometry(QRect(20, 155, 681, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAge_hor.setObjectName("btnAge_hor")
        self.horizontalLayout_2.addWidget(self.btnAge_hor)
        self.btnAtu_hor.setObjectName("btnAtu_hor")
        self.horizontalLayout_2.addWidget(self.btnAtu_hor)
        self.btnExc_hor.setObjectName("btnExc_hor")
        self.horizontalLayout_2.addWidget(self.btnExc_hor)
        self.BtnImp_hor.setObjectName("BtnImp_hor")
        self.horizontalLayout_2.addWidget(self.BtnImp_hor)
        self.btnLim_hor.setObjectName("btnLim_hor")
        self.horizontalLayout_2.addWidget(self.btnLim_hor)
        self.layoutWidget2.setGeometry(QRect(20, 230, 681, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtPesNom_hor.setClearButtonEnabled(True)
        self.txtPesNom_hor.setObjectName("txtPesNom_hor")
        self.horizontalLayout_3.addWidget(self.txtPesNom_hor)
        self.btnPesNom_hor.setObjectName("btnPesNom_hor")
        self.horizontalLayout_3.addWidget(self.btnPesNom_hor)
        self.txtPesDat_hor.setClearButtonEnabled(True)
        self.txtPesDat_hor.setObjectName("txtPesDat_hor")
        self.horizontalLayout_3.addWidget(self.txtPesDat_hor)
        self.btnPesDat_hor.setObjectName("btnPesDat_hor")
        self.horizontalLayout_3.addWidget(self.btnPesDat_hor)
        self.listPesCli = QListWidget(self.tabHor)
        self.listPesCli.setGeometry(QRect(20, 47, 338, 91))
        self.listPesCli.setObjectName("listPesCli")
        self.tabWidget.addTab(self.tabHor, "")
        self.tabCli.setObjectName("tabCli")
        self.layoutWidget3.setGeometry(QRect(120, 230, 481, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txtPesNom_cli.setClearButtonEnabled(True)
        self.txtPesNom_cli.setObjectName("txtPesNom_cli")
        self.horizontalLayout_4.addWidget(self.txtPesNom_cli)
        self.btnPesNom_cli.setObjectName("btnPesNom_cli")
        self.horizontalLayout_4.addWidget(self.btnPesNom_cli)
        self.table_cli.setGeometry(QRect(20, 280, 681, 211))
        self.table_cli.setObjectName("table_cli")
        self.table_cli.setColumnCount(6)
        self.table_cli.setRowCount(0)
        delegate_cli = ReadOnlyDelegate(self.table_cli)
        item = QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(0, item)
        self.table_cli.setItemDelegateForColumn(0, delegate_cli)
        item = QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(1, item)
        self.table_cli.setItemDelegateForColumn(1, delegate_cli)
        item = QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(2, item)
        self.table_cli.setItemDelegateForColumn(2, delegate_cli)
        item = QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(3, item)
        self.table_cli.setItemDelegateForColumn(3, delegate_cli)
        item = QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(4, item)
        self.table_cli.setItemDelegateForColumn(4, delegate_cli)
        item = QTableWidgetItem()
        self.table_cli.setHorizontalHeaderItem(5, item)
        self.table_cli.setItemDelegateForColumn(5, delegate_cli)
        self.layoutWidget_2.setGeometry(QRect(20, 155, 681, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnSal_cli.setObjectName("btnSal_cli")
        self.horizontalLayout_5.addWidget(self.btnSal_cli)
        self.btnAtu_cli.setObjectName("btnAtu_cli")
        self.horizontalLayout_5.addWidget(self.btnAtu_cli)
        self.btnExc_cli.setObjectName("btnExc_cli")
        self.horizontalLayout_5.addWidget(self.btnExc_cli)
        self.btnLim_cli.setObjectName("btnLim_cli")
        self.horizontalLayout_5.addWidget(self.btnLim_cli)
        self.layoutWidget_3.setGeometry(QRect(20, 10, 681, 141))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txtNom_cli.setClearButtonEnabled(True)
        self.txtNom_cli.setObjectName("txtNom_cli")
        self.verticalLayout_3.addWidget(self.txtNom_cli)
        self.cbcSex_cli.setObjectName("cbcSex_cli")
        self.cbcSex_cli.addItem('Indefinido')
        self.cbcSex_cli.addItem('Femenino')
        self.cbcSex_cli.addItem('Masculino')
        self.verticalLayout_3.addWidget(self.cbcSex_cli)
        self.txtCpf_cli.setClearButtonEnabled(True)
        self.txtCpf_cli.setObjectName("txtCpf_cli")
        self.verticalLayout_3.addWidget(self.txtCpf_cli)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txtId_cli.setObjectName("txtId_cli")
        self.verticalLayout_4.addWidget(self.txtId_cli)
        self.txtEnd_cli.setObjectName("txtEnd_cli")
        self.verticalLayout_4.addWidget(self.txtEnd_cli)
        self.txtFon_cli.setObjectName("txtFon_cli")
        self.verticalLayout_4.addWidget(self.txtFon_cli)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.line_2.setGeometry(QRect(20, 210, 681, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tabCli, "")
        self.tabSer.setObjectName("tabSer")
        self.layoutWidget_4.setGeometry(QRect(120, 230, 481, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_9.setClearButtonEnabled(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_7.addWidget(self.lineEdit_9)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_7.addWidget(self.pushButton_15)
        self.table_ser.setGeometry(QRect(20, 280, 681, 211))
        self.table_ser.setObjectName("table_ser")
        self.table_ser.setColumnCount(5)
        self.table_ser.setRowCount(0)
        delegate_ser = ReadOnlyDelegate(self.table_ser)
        item = QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(0, item)
        self.table_ser.setItemDelegateForColumn(0, delegate_ser)
        item = QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(1, item)
        self.table_ser.setItemDelegateForColumn(1, delegate_ser)
        item = QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(2, item)
        self.table_ser.setItemDelegateForColumn(2, delegate_ser)
        item = QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(3, item)
        self.table_ser.setItemDelegateForColumn(3, delegate_ser)
        item = QTableWidgetItem()
        self.table_ser.setHorizontalHeaderItem(4, item)
        self.table_ser.setItemDelegateForColumn(4, delegate_ser)
        self.layoutWidget_5.setGeometry(QRect(20, 155, 681, 51))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_8.addWidget(self.pushButton_17)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_8.addWidget(self.pushButton_18)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_8.addWidget(self.pushButton_19)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_8.addWidget(self.pushButton_21)
        self.layoutWidget_6.setGeometry(QRect(20, 10, 681, 141))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.txtNom_ser.setClearButtonEnabled(True)
        self.txtNom_ser.setObjectName("txtNom_ser")
        self.verticalLayout_5.addWidget(self.txtNom_ser)
        self.cbbPro_ser.setObjectName("cbbPro_ser")
        self.verticalLayout_5.addWidget(self.cbbPro_ser)
        self.txtSer_ser.setClearButtonEnabled(True)
        self.txtSer_ser.setObjectName("txtSer_ser")
        self.verticalLayout_5.addWidget(self.txtSer_ser)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.txtId_ser.setObjectName("txtId_ser")
        self.verticalLayout_6.addWidget(self.txtId_ser)
        self.horHor_ser.setObjectName("horHor_ser")
        self.verticalLayout_6.addWidget(self.horHor_ser)
        spacerItem = QSpacerItem(
            20, 45, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.line_3.setGeometry(QRect(20, 210, 681, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tabWidget.addTab(self.tabSer, "")
        self.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QRect(0, 0, 750, 28))
        self.menubar.setObjectName("menubar")
        self.menuAtendimentos.setObjectName("menuAtendimentos")
        self.menuClientes.setObjectName("menuClientes")
        self.menuHor_rios.setObjectName("menuHor_rios")
        self.menuServi_os.setObjectName("menuServi_os")
        self.menuSair.setObjectName("menuSair")
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionHor_rios.setObjectName("actionHor_rios")
        self.actionClientes.setObjectName("actionClientes")
        self.actionServi_os.setObjectName("actionServi_os")
        self.actionUsu_rios.setObjectName("actionUsu_rios")
        self.actionClientes_2.setObjectName("actionClientes_2")
        self.actionHor_rios_2.setObjectName("actionHor_rios_2")
        self.actionServi_os_2.setObjectName("actionServi_os_2")
        self.actionAjuda.setObjectName("actionAjuda")
        self.actionAddHor.setObjectName("actionAddHor")
        self.actionSair_2.setObjectName("actionSair_2")
        self.menuAtendimentos.addAction(self.actionHor_rios)
        self.menuAtendimentos.addAction(self.actionClientes)
        self.menuAtendimentos.addAction(self.actionServi_os)
        self.menuClientes.addAction(self.actionUsu_rios)
        self.menuHor_rios.addAction(self.actionHor_rios_2)
        self.menuHor_rios.addAction(self.actionClientes_2)
        self.menuHor_rios.addAction(self.actionServi_os_2)
        self.menuServi_os.addAction(self.actionAjuda)
        self.menuServi_os.addAction(self.actionAddHor)
        self.menuSair.addAction(self.actionSair_2)
        self.menubar.addAction(self.menuAtendimentos.menuAction())
        self.menubar.addAction(self.menuHor_rios.menuAction())
        self.menubar.addAction(self.menuClientes.menuAction())
        self.menubar.addAction(self.menuServi_os.menuAction())
        self.menubar.addAction(self.menuSair.menuAction())
        self.txtCpf_cli.setInputMask('###.###.###-##')
        self.txtFon_cli.setInputMask('(##) #####-####')
        self.txtSer_ser.setInputMask('R$#.###,##')
        self.horHor_ser.setInputMask('#:##min')
        self.horHor_ser.setText('n')

        # largura padrao das tabelas
        self.table_hor.setColumnWidth(0, 50)
        self.table_hor.setColumnWidth(1, 180)
        self.table_hor.setColumnWidth(5, 120)
        self.table_cli.setColumnWidth(0, 50)
        self.table_cli.setColumnWidth(1, 190)
        self.table_ser.setColumnWidth(0, 50)
        self.table_ser.setColumnWidth(1, 200)
        self.table_ser.setColumnWidth(2, 200)

        # desativar botões por padrao
        self.txtId_hor.setEnabled(False)
        self.btnAtu_hor.setEnabled(False)
        self.btnExc_hor.setEnabled(False)
        self.txtId_cli.setEnabled(False)
        self.btnAtu_cli.setEnabled(False)
        self.btnExc_cli.setEnabled(False)
        self.txtId_ser.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        self.pushButton_19.setEnabled(False)
        self.listPesCli.setVisible(False)
        # self.listPesCli.setEnabled(False)

        # conectar funçoes com componentes da view
        self.actionUsu_rios.triggered.connect(self.open_users_screens)
        self.actionSair_2.triggered.connect(self.closeEvent)
        self.actionClientes.triggered.connect(self.on_menu_clientes)
        self.actionHor_rios.triggered.connect(self.on_menu_horarios)
        self.actionServi_os.triggered.connect(self.on_menu_servicos)
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
        self.btnPesNom_hor.clicked.connect(self.pesquisar_horarios)
        self.txtPesNom_hor.textChanged.connect(self.pesquisar_horarios)
        self.btnPesDat_hor.clicked.connect(self.pesq_hor_by_date)
        self.txtPesDat_hor.textChanged.connect(self.pesq_hor_by_date)
        self.tabWidget.currentChanged.connect(self.popula_todas_tabelas)
        self.txtPesCli_hor.textChanged.connect(self.popula_list_cli)
        self.listPesCli.clicked.connect(self.get_item_selected)
        # self.cbbHor_hor.currentTextChanged.connect(self.call_popula_hor)
        # self.cbbHor_hor.activated.connect(self.call_popula_hor)

        self.table_cli.clicked.connect(self.setar_campos_cli)
        self.table_ser.clicked.connect(self.setar_campos_ser)
        self.table_hor.clicked.connect(self.setar_campos_hor)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate(
            "MainWindow", "Tela Principal - Mehsys"))
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
        self.txtPesCli_hor.setPlaceholderText(
            _translate("MainWindow", "Pesquisar cliente"))
        self.cbbSer_hor.setPlaceholderText(
            _translate("MainWindow", "Selecionar serviço"))
        self.cbbPro_hor.setPlaceholderText(
            _translate("MainWindow", "Selecionar Profissional"))
        self.txtId_hor.setPlaceholderText(_translate("MainWindow", "Id"))
        self.cbbHor_hor.setPlaceholderText(
            _translate("MainWindow", "Selecionar horário"))
        self.btnAge_hor.setText(_translate("MainWindow", "Agendar"))
        self.btnAtu_hor.setText(_translate("MainWindow", "Atualizar"))
        self.btnExc_hor.setText(_translate("MainWindow", "Excluir"))
        self.BtnImp_hor.setText(_translate("MainWindow", "Imprimir"))
        self.btnLim_hor.setText(_translate("MainWindow", "Limpar"))
        self.txtPesNom_hor.setPlaceholderText(
            _translate("MainWindow", "Nome cliente"))
        self.btnPesNom_hor.setText(_translate("MainWindow", "Pesquisar"))
        self.txtPesDat_hor.setPlaceholderText(
            _translate("MainWindow", "Data agendamento"))
        self.btnPesDat_hor.setText(_translate("MainWindow", "Pesquisar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabHor), _translate("MainWindow", "Horários"))
        self.txtPesNom_cli.setPlaceholderText(
            _translate("MainWindow", "Nome cliente"))
        self.btnPesNom_cli.setText(_translate("MainWindow", "Pesquisar"))
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
        self.btnSal_cli.setText(_translate("MainWindow", "Salvar"))
        self.btnAtu_cli.setText(_translate("MainWindow", "Atualizar"))
        self.btnExc_cli.setText(_translate("MainWindow", "Excluir"))
        self.btnLim_cli.setText(_translate("MainWindow", "Limpar"))
        self.txtNom_cli.setPlaceholderText(
            _translate("MainWindow", "Nome cliente"))
        self.cbcSex_cli.setPlaceholderText(
            _translate("MainWindow", "Selecionar sexo"))
        self.txtCpf_cli.setPlaceholderText(
            _translate("MainWindow", "CPF cliente"))
        self.txtId_cli.setPlaceholderText(_translate("MainWindow", "Id"))
        self.txtEnd_cli.setPlaceholderText(
            _translate("MainWindow", "Endereço cliente"))
        self.txtFon_cli.setPlaceholderText(
            _translate("MainWindow", "Fone cliente"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabCli), _translate("MainWindow", "Clientes"))
        self.lineEdit_9.setPlaceholderText(
            _translate("MainWindow", "Nome serviço"))
        self.pushButton_15.setText(_translate("MainWindow", "Pesquisar"))
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
        self.pushButton_17.setText(_translate("MainWindow", "Salvar"))
        self.pushButton_18.setText(_translate("MainWindow", "Atualizar"))
        self.pushButton_19.setText(_translate("MainWindow", "Excluir"))
        self.pushButton_21.setText(_translate("MainWindow", "Limpar"))
        self.txtNom_ser.setPlaceholderText(
            _translate("MainWindow", "Nome serviço"))
        self.cbbPro_ser.setPlaceholderText(
            _translate("MainWindow", "Selecionar profissional"))
        self.txtSer_ser.setPlaceholderText(
            _translate("MainWindow", "Valor serviço"))
        self.txtId_ser.setPlaceholderText(_translate("MainWindow", "Id"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabSer), _translate("MainWindow", "Serviços"))
        self.menuAtendimentos.setTitle(
            _translate("MainWindow", "Atendimentos"))
        self.menuClientes.setTitle(_translate("MainWindow", "Usuários"))
        self.menuHor_rios.setTitle(_translate("MainWindow", "Relatórios"))
        self.menuServi_os.setTitle(_translate("MainWindow", "Opções"))
        self.menuSair.setTitle(_translate("MainWindow", "Sair"))
        self.actionHor_rios.setText(_translate("MainWindow", "Horários"))
        self.actionClientes.setText(_translate("MainWindow", "Clientes"))
        self.actionServi_os.setText(_translate("MainWindow", "Serviços"))
        self.actionUsu_rios.setText(_translate("MainWindow", "Usuários"))
        self.actionClientes_2.setText(_translate("MainWindow", "Clientes"))
        self.actionHor_rios_2.setText(_translate("MainWindow", "Horários"))
        self.actionServi_os_2.setText(_translate("MainWindow", "Serviços"))
        self.actionAjuda.setText(_translate("MainWindow", "Ajuda"))
        self.actionAddHor.setText(_translate(
            "MainWindow", "Adicionar horários"))
        self.actionSair_2.setText(_translate("MainWindow", "Sair"))

    # pergunta para sair do programa
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Sair?", "Tem certeza que quer Sair?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(0)
        else:
            event.ignore()

    # def keyPressEvent(self, event):
    #     if event.key() and self.cbbPro_hor.currentText() != '' and self.cbbPro_hor.currentText() != 'Selecionar' \
    #             and self.cbbHor_hor.currentIndex() < 0 \
    #             and self.dat_hor.text() != '01/01/2000':
    #         print('evento')
    #         self.popula_cbb_horarios(self.cbbPro_hor.currentText(), self.dat_hor.text())

    # popula horários somente quando outros campos obrigatórios estão preenchidos e o horário não está no cliq do mouse
    def mousePressEvent(self, event):
        if event.buttons() and self.cbbPro_hor.currentText() != '' and self.cbbPro_hor.currentText() != 'Selecionar' \
                and self.cbbHor_hor.currentIndex() < 0 \
                and self.dat_hor.text() != '01/01/2000':
            print('evento')
            self.popula_cbb_horarios(self.cbbPro_hor.currentText(), self.dat_hor.text())

    # centralizar tela
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def keyPressEvent(self, event):
    #     print("Pressionado!!!")

    def open_users_screens(self):
        self.window = QMainWindow()
        self.ui = UiUsuario()
        self.ui.setupUi(self.window)
        self.window.show()

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
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'update tbclientes set nome=?, sexo=?, cpf=?, endereco=?, fone=? where id=?'
        nome = self.txtNom_cli.text()
        sexo = self.cbcSex_cli.currentText()
        cpf = self.txtCpf_cli.text()
        endereco = self.txtEnd_cli.text()
        fone = self.txtFon_cli.text()
        id = self.txtId_cli.text()
        try:
            if len(nome.strip()) < 4 or len(cpf.strip()) < 14 or len(fone.strip()) < 14:
                QMessageBox.warning(self, 'Preencha os campos', 'Preencha os campos obrigatórios para atualizar dados '
                                                                'do cliente')
            else:
                cursor.execute(sql, [nome, sexo, cpf, endereco, fone, id])
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
            self.txtNom_cli.setText(self.table_cli.item(r, 1).text())
            self.cbcSex_cli.setCurrentText(self.table_cli.item(r, 2).text())
            self.txtCpf_cli.setText(self.table_cli.item(r, 3).text())
            self.txtEnd_cli.setText(self.table_cli.item(r, 4).text())
            self.txtFon_cli.setText(self.table_cli.item(r, 5).text())
        self.btnSal_cli.setEnabled(False)
        self.btnAtu_cli.setEnabled(True)
        self.btnExc_cli.setEnabled(True)

    # METODOS TAB SERVIÇOS -----------------------------------------------------------

    # Adicionar novo serviço
    def on_btn_sal_ser_pressed(self):
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'insert into tbservicos(nome, usuario, valor, duracao) values(?,?,?,?)'
        nome = self.txtNom_ser.text()
        prof = self.cbbPro_ser.currentText()
        valor = self.txtSer_ser.text()
        print(valor[2:3])
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
        nome = self.txtNom_ser.text()
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
                    self, 'SUCESSO!!!', f'Cliente ({self.txtNom_ser.text()}) EXCLUIDO com Sucesso!')
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
            self.txtNom_ser.setText(self.table_ser.item(r, 1).text())
            self.cbbPro_ser.setCurrentText(self.table_ser.item(r, 2).text())
            self.txtSer_ser.setText(self.table_ser.item(r, 3).text())
            self.horHor_ser.setText(self.table_ser.item(r, 4).text())
        self.pushButton_17.setEnabled(False)
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

    # METODOS TAB HORÁRIOS -----------------------------------------------------------

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
        rows = sorted(set(index.row() for index in self.table_hor.selectedIndexes()))
        for r in rows:
            self.txtId_hor.setText(self.table_hor.item(r, 0).text())
            self.txtPesCli_hor.setText(self.table_hor.item(r, 1).text())
            self.cbbSer_hor.setCurrentText(self.table_hor.item(r, 2).text())
            y = int(self.table_hor.item(r, 3).text()[6:])
            m = int(self.table_hor.item(r, 3).text()[3:5])
            d = int(self.table_hor.item(r, 3).text()[:2])
            data = QDate(y, m, d)
            self.dat_hor.setDate(data)
            self.cbbHor_hor.setCurrentText(self.table_hor.item(r, 4).text())
            self.cbbPro_hor.setCurrentText(self.table_hor.item(r, 5).text())

    # pesquisa clientes para o campo de texto txtPesCli_hor
    def popula_list_cli(self):
        self.listPesCli.clear()
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = "select nome from tbclientes where nome like ? order by nome"
        search = '%' + self.txtPesCli_hor.text() + '%'
        try:
            cursor.execute(sql, [search])
            rs = cursor.fetchall()
            v = 0
            if len(rs) == 1:
                self.listPesCli.addItem(rs[0][0])
                v = 1
            elif len(rs) == 2:
                self.listPesCli.addItem(rs[0][0])
                self.listPesCli.addItem(rs[1][0])
                v = 2
            elif len(rs) == 3:
                self.listPesCli.addItem(rs[0][0])
                self.listPesCli.addItem(rs[1][0])
                self.listPesCli.addItem(rs[2][0])
                v = 3
            elif len(rs) == 4:
                self.listPesCli.addItem(rs[0][0])
                self.listPesCli.addItem(rs[1][0])
                self.listPesCli.addItem(rs[2][0])
                self.listPesCli.addItem(rs[3][0])
                v = 4
            else:
                while len(rs) > 0 and v <= 4:
                    self.listPesCli.addItem(rs[v][0])
                    v += 1
            db.close()

            if v >= 1:
                self.listPesCli.setVisible(True)
            else:
                self.listPesCli.setVisible(False)

        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # obter valor da lista
    def get_item_selected(self):
        print(self.listPesCli.currentItem().text())
        self.txtPesCli_hor.setText(self.listPesCli.currentItem().text())
        self.listPesCli.setVisible(False)

    # popula combobox serviços
    def popula_cbb_servicos(self):
        self.cbbSer_hor.clear()
        self.cbbSer_hor.addItem("Selecionar")
        self.cbbSer_hor.setCurrentIndex(0)
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = 'select nome, id from tbservicos order by nome'
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
            for i in range(len(rs)):
                self.cbbSer_hor.addItem(rs[i][0] + '  - ' + str(rs[i][1]))
            db.close()
        except Exception as e:
            db.close()
            QMessageBox.warning(self, 'ERRO!!!', str(e))

    # popula combobox de horários de atendimento
    def popula_cbb_horarios(self, profissional, data):
        self.cbbHor_hor.clear()
        self.cbbHor_hor.addItem("Selecionar")
        self.cbbHor_hor.setCurrentIndex(0)
        db = sqlite3.connect('dbmehsys.db')
        cursor = db.cursor()
        sql = "select p.* from (select '" \
              + data + "' data, '" + profissional + \
              "' funcionario, horario from " \
              "horarios) p left join " \
              "horarios_agendados c on " \
              "p.horario=c.horario and " \
              "p.data=c.data and " \
              "p.funcionario=c.funcionario where " \
              "c.data is null "
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


app = QApplication(sys.argv)
principal = QMainWindow()
