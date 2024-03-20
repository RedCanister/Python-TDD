from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self.nome

    @property
    def salario(self):
        return self.salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = int(data_nascimento_quebrada[-1])
        ano_atual = date.today().year
        return ano_atual - ano_nascimento

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split(' ')
        print(nome_quebrado)
        return nome_quebrado[-1]

    def _is_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato',
                      'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self._salario >= 100000) and (self. sobrenome() in sobrenomes)


    def decrescimo_salario(self):

        if self._is_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

        return self._salario

    def calcular_bonus(self):
        valor = self.salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self.nome}, {self._data_nascimento}, {self.salario})'
