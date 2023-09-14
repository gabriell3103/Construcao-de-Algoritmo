# EXERCÍCIO 5.29
# Escreva um programa que crie um dicionário relacionando o nome dos estados brasileiros (como chaves) às suas siglas.
# O programa deve perguntar ao usuário o nome de um estado e chamar uma função que devolva a sua sigla.
# O nome do estado pode estar em maiúsculas ou minúsculas e mesmo assim o programa deve dar a resposta correta.
# (Nota: para transformar todas as letras de uma string em minúsculas, use a função lower(). Assim, se palavra = ‘PalavrA’, palavra.lower() devolve ‘palavra’.)

estados = {'acre': 'AC','alagoas': 'AL','amapá': 'AP','amazonas': 'AM','bahia': 'BA','ceará': 'CE','distrito federal': 'DF','espírito santo': 'ES',
    'goiás': 'GO','maranhão': 'MA','mato grosso': 'MT','mato grosso do sul': 'MS','minas gerais': 'MG','pará': 'PA','paraíba': 'PB','paraná': 'PR',
    'pernambuco': 'PE','piauí': 'PI','rio de janeiro': 'RJ','rio grande do norte': 'RN','rio grande do sul': 'RS','rondônia': 'RO','roraima': 'RR',
    'santa catarina': 'SC','são paulo': 'SP','sergipe': 'SE','tocantins': 'TO'}

def obter_sigla(estado):
    estado = estado.lower()
    return estados.get(estado, 'Esse estado não exixte')


estado = input("Digite o nome do estado: ")

sigla = obter_sigla(estado)
print(f"A sigla de {estado.capitalize()} é {sigla.upper()}.")