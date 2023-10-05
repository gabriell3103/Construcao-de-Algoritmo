# EXERCÍCIO 6.8
# O Programa 6.10 só funciona bem com um nome composto de três partes. Modifique o programa para que seja possível trabalhar com um número maior de partes.

def nome_formatado(nome: str) -> str:
    partes_do_nome = nome.split()

    if len(partes_do_nome) >= 2:
        sobrenome = partes_do_nome[-1]
        primeiro_nome = partes_do_nome[0]
        inicial_segundo_nome = partes_do_nome[1][0] if len(
            partes_do_nome) > 2 else ''

        partes_adicionais = " ".join(partes_do_nome[2:])

        nome_formatado = f"{sobrenome}, {primeiro_nome} {inicial_segundo_nome}. {partes_adicionais}"
        return nome_formatado
    else:
        return "Nome inválido"
    
nome = 'Gabriel Eduardo Alves da Silva'
formatar_nome = nome_formatado(nome)
print(formatar_nome)