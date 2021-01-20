import sqlite3


class CreateBdSqlite:

    def __init__(self):
        self.connect = sqlite3.connect("dbmehsys.db")
        self.cursor = self.connect.cursor()

    def create_tables(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS utils (current_user INTEGER)")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tbusuarios (\
                                        id	INTEGER NOT NULL,\
                                        usuario	TEXT NOT NULL,\
                                        fone	TEXT NOT NULL,\
                                        login	TEXT NOT NULL,\
                                        senha	TEXT NOT NULL,\
                                        perfil	TEXT NOT NULL,\
                                        hora_in	TEXT DEFAULT NULL,\
                                        hora_out	TEXT DEFAULT NULL,\
                                        PRIMARY KEY(id));")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS horarios ("
                                + "horario	TEXT NOT NULL UNIQUE"
                                + ");")

            self.cursor.execute("CREATE UNIQUE INDEX horario ON horarios ("
                                + "	horario"
                                + ");")
            self.cursor.execute("INSERT INTO tbusuarios ("
                                + "usuario, fone, login, senha, perfil, hora_in, hora_out) "
                                + "VALUES ('trocar senha', '(00)00000-0000', 'admin', '1234', 'admin', '00:00', '00:00');")
            self.cursor.execute("INSERT INTO horarios (horario) "
                                + "VALUES ('08:00'), ('08:15'), ('08:30'), ('08:45'), ('09:00'), "
                                + "('09:15'), ('09:30'), ('09:45'), ('10:00'), ('10:15'), "
                                + "('10:30'), ('10:45'), ('11:00'), ('11:15'), ('11:30'), "
                                + "('11:45'), ('13:00'), ('13:15'), ('13:30'), ('13:45'), "
                                + "('14:00'), ('14:15'), ('14:30'), ('14:45'), ('15:00'), "
                                + "('15:15'), ('15:30'), ('15:45'), ('16:00'), ('16:15'), "
                                + "('16:30'), ('16:45');")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tbservicos ("
                                + "id	INTEGER NOT NULL UNIQUE, "
                                + "nome TEXT NOT NULL, "
                                + "usuario	TEXT NOT NULL, "
                                + "valor	TEXT NOT NULL, "
                                + "duracao	TEXT DEFAULT NULL, "
                                + "PRIMARY KEY(id AUTOINCREMENT)"
                                + ");")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS horarios_agendados ("
                                + "	data	TEXT NOT NULL,"
                                + "	funcionario	TEXT NOT NULL,"
                                + "	horario	TEXT NOT NULL"
                                + ");")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tbclientes ("
                                + "	id	INTEGER NOT NULL UNIQUE,"
                                + "	nome	TEXT NOT NULL,"
                                + "	sexo	TEXT DEFAULT NULL,"
                                + "	cpf	TEXT NOT NULL,"
                                + "	endereco	TEXT NOT NULL,"
                                + "	fone	TEXT NOT NULL,"
                                + "	PRIMARY KEY(id AUTOINCREMENT)"
                                + ");")
            self.cursor.execute("CREATE UNIQUE INDEX agendamento ON horarios_agendados ("
                                + "	data,"
                                + "	funcionario,"
                                + "	horario"
                                + ");")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tbhorarios ("
                                + "	id	INTEGER NOT NULL,"
                                + "	cliente	TEXT NOT NULL,"
                                + "	servico	TEXT NOT NULL,"
                                + "	data	TEXT NOT NULL,"
                                + "	horario	TEXT NOT NULL,"
                                + "	profissional	TEXT NOT NULL,"
                                + "	id_ser	INTEGER DEFAULT NULL,"
                                + "	FOREIGN KEY(id_ser) REFERENCES tbservicos(id),"
                                + "	PRIMARY KEY(id AUTOINCREMENT)"
                                + ");")
            self.cursor.execute("INSERT INTO tbclientes ("
                                + "nome, sexo, cpf, endereco, fone) "
                                + "VALUES ('teste deletar', 'Indefinido', '000.000.000-00', '', '(00)00000-0000');")
            self.cursor.execute("INSERT INTO tbservicos ("
                                + "nome, usuario, valor, duracao) "
                                + "VALUES ('teste deletar', '', 'R$0.020,00', '0:10min');")
            self.cursor.execute("INSERT INTO tbhorarios ("
                                + "cliente, servico, data, horario, profissional, id_ser) "
                                + "VALUES ('teste deletar', 'teste deletar  - 1', '10/01/2021', '09:00', 'admin', '1');")
            self.connect.commit()
            print("banco criado")

            self.cursor.close()
            self.connect.close()
        except Exception as e:
            print(e)
