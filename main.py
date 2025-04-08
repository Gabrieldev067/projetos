#------------------------------SISTEMA DE CHAT DE MENSAGEM-----------------------------------------

import os

mensagens=[]

nome=input('Nome: ')

while True:
    os.system('cls')

    if len(mensagens)>0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print('__'*5)

    texto=input('Mensagem: ')
    if texto=='fim':
        break

    mensagens.append({
        'nome': nome,
        'texto': texto
    })