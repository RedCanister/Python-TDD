from codigo.bytebank import Funcionario
import pytest


class TestClass:

    def test_quando_idade_recebe_16_04_199_deve_retornar_25(self):

        # Given - Contexto
        entrada = '16/04/1999' 
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        
        # When - Ação
        resultado = funcionario_teste.idade()

        # Then - desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_jorge_kayode_deve_retornar_kayode(self):
        entrada = 'Jorge Kayodê'
        esperado = 'Kayodê'

        funcionario_teste = Funcionario(entrada, '16/04/1999', 1111)

        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado

    def test_quando_decresscimo_salario_recebe_100000_deve_retornar_90000(self):

        # Given - Contexto
        entrada_salario = 100000
        entrada_nome = 'Paula Bragança'

        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2111', entrada_salario)

        # When - Ação
        resultado = funcionario_teste.decrescimo_salario()

        # Then - desfecho
        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # Given - Contexto
        entrada_salario = 10001
        entrada_nome = 'Paula Bragança'

        esperado = 100

        funcionario_teste = Funcionario(entrada_nome, '11/11/2111', entrada_salario)

        # When - Ação
        resultado = funcionario_teste.calcular_bonus()

        # Then - desfecho
        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 10000000

            esperado = 100

            funcionario_teste = Funcionario('teste', '11/11/2111', entrada_salario)

            # When - Ação
            resultado = funcionario_teste.calcular_bonus()

            # Then - desfecho
            assert resultado