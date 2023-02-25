nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

qtd_letras = len(nome)

if nome and idade.capitalize():
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {qtd_letras} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')