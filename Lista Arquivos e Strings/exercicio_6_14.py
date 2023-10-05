# EXERCÍCIO 6.14
# Escreva um programa que copie o conteúdo de um arquivo para um novo arquivo. 
# Seu programa deve testar se o arquivo de destino já existe e, se afirmativo, deve perguntar ao usuário se ele quer sobrescrevê-lo.

import os

def copiar_arquivo(origem: str, destino: str) -> None:
    try:
        with open(origem, 'r') as arquivo_origem:
            with open(destino, 'w') as arquivo_destino:
                conteudo = arquivo_origem.read()
                
                arquivo_destino.write(conteudo)

        print(f'O arquivo foi copiado com sucesso para {destino}.')
    except FileNotFoundError:
        print(f'O arquivo de origem "{origem}" não foi encontrado.')
    except PermissionError:
        print(f'Não foi possível copiar o arquivo. Verifique as permissões.')
    except Exception as e:
        print(f'Ocorreu um erro ao copiar o arquivo: {str(e)}')


def main() -> None:
    origem = input('Informe o nome do arquivo de origem: ')
    destino = input('Informe o nome do arquivo de destino: ')

    if origem == destino:
        print('O arquivo de origem e destino não podem ser iguais.')
        return

    try:
        if os.path.exists(destino):
            resposta = input(
                f'O arquivo "{destino}" já existe. Deseja sobrescrevê-lo? (S/N): ')
            if resposta.lower() != 's':
                print('Operação cancelada.')
                return

        copiar_arquivo(origem, destino)
    except KeyboardInterrupt:
        print('Operação cancelada pelo usuário.')
    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')


main()