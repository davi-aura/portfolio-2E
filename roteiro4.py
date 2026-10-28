def somar (valor_principal, acréscimo):
    return valor_principal + acréscimo



def testar_operacao_soma():
    # Arrange
    valor1 = 100.0
    valor2 = 50.0
    # Act
    resultado = somar(valor1, valor2)
    # Assert
    assert resultado == 150.0, "A soma falhou!"
    print("Teste de Soma: PASSOU!")

testar_operacao_soma()


def subtrair (valor_principal, acrescimo):
    return valor_principal - acrescimo


def testar_operacao_subtrair():
    # Arrange
    valor1 = 100.0
    valor2 = 50.0
    # Act
    resultado = subtrair(valor1, valor2)
    # Assert
    assert resultado == 50.0, "A subtração falhou!"
    print("Teste de subtração: PASSOU!")

testar_operacao_subtrair()                                                                                 

