from Utils import ConexaoSQLite
from login import UiLoginWindow as login


class LoginCtrl:
    conn = ConexaoSQLite.ConexaoSQLite()
    login = login()

    def __init__(self):
        self.db = self.conn.getConexao()
        self.cursor = self.db.cursor()

    def login_entry(self):
        sql = "select * from tbusuarios where login=? and senha=?"
        self.rs = self.cursor.execute(sql, [self.login.txtUser.text(), self.login.txtPass.text()])
        if len(self.cursor.fetchall() > 0):
            print("pegou")
        else:
            print("não pegou")
