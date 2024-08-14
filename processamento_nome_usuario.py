# Nome e idade 
nome = input('Digite seu  nome: ') # Digite seu nome
idade = int(input('Digite sua idade: ')) # Digite sua idade


if nome and idade: # se a pessoa digitar nome E idade and = "E"
    print(f'Seu nome é {nome}') # seu nom é nome digitado
    print(f'Seu nome invertido é {nome[::-1]}') # o nome digitador invertido


    if ' ' in nome: 
        #' ': Esta parte representa um caractere de espaço em branco, verificando se o nome tem espaços
        #in: O operador in é utilizado para verificar se um determinado valor (neste caso, o espaço ' ') está presente dentro de uma sequência, como uma string, lista, ou outros tipos iteráveis.
        print('Seu nome contém (ou não) espaços ')

    else:
        print('Seu nome não contém espaços ')

        print(f'Seu nome tem {len(nome)}letras ') # Quantidade de letras no nome
        print(f'A primeira letra do seu nome é {nome[0]} ') # Primeira letra do nome 
        print(f'A última letra do seu nome é {nome[-1]} ') # Última letra do nome

else:   

    print("Desculpe, você deixou campos vazios. ") 