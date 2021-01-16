import sqlite3


class ConexaoSQLite:
    conexao = False

    def conectar(self):
        try:
            self.conexao = sqlite3.connect('../dbmehsys.db')
            print('Conectado')
            return True
        except Exception as e:
            print(e)
            return False

    def desconectar(self):
        try:
            if self.conexao == 0:
                self.conexao.close()
                print('desconectado')
        except Exception as e:
            print(e)
            return False
        return True

    def getConexao(self):
        return self.conexao


