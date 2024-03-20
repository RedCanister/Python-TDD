from codigo import bytebank
from codigo.bytebank import Funcionario

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