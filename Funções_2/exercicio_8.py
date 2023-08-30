def calcular_desconto(valor, porcentagem):
    desconto = valor * (porcentagem/100)
    return valor - desconto

valor = 1500
porcentagem_desconto = 30

desconto = print(f'O valor com desconto será: {calcular_desconto(valor, porcentagem_desconto)}')