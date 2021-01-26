class Valida:

    def __init__(self):
        self.cpf_numerado = []

    def validaCPf(self, num):
        self.numerar_cpf(num)
        if self.primeiro_digito() == True and self.segundo_digito() == True:
            return True
        else:
            return False

    def primeiro_digito(self):
        acumulador = 0
        controlador = 10
        for nums in self.cpf_numerado[:9]:
            result = int(nums) * controlador
            acumulador += result
            controlador = controlador - 1
        acumulador = acumulador * 10 % 11
        if acumulador == 10:
            acumulador = 0
        if acumulador == int(self.cpf_numerado[9]):
            return True
        else:
            return False

    def segundo_digito(self):
        acumulador = 0
        controlador = 11
        for nums in self.cpf_numerado[:10]:
            result = int(nums) * controlador
            acumulador += result
            controlador = controlador - 1
        acumulador = acumulador * 10 % 11
        if acumulador == 10:
            acumulador = 0
        if acumulador == int(self.cpf_numerado[10]):
            return True
        else:
            return False

    def numerar_cpf(self, num):
        cpf = str(num.replace('.', '').replace('-', ''))
        for d in cpf:
            self.cpf_numerado.append(d)
