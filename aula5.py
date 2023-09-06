import time

class Gerenciamento():
    def atualizar():
        print('Atualizar')
    def analise():
        print('Analise')
    def enviar():
        print('Enviar')
    def aprovado():
        print('Aprovado')
    def atualizando():
        print('Atualizando')
    def cancelado():
        print('Cancelado')
 

codigo = int(input('Informe o código :'))
item = str(input('Informe o produto :'))
valor = float(input('Informe o valor do produto :'))
quantidade = int(input('Quantidade do Produto :'))

def venda():
    pedido = [item, valor, quantidade]
    soma = valor * quantidade
    print(f'Item: {pedido} Valor Total : {soma}')



time.sleep(1)
print('|------------API COMERCE-------------|')
time.sleep(0.5)

def api():
    if codigo > 1 and codigo < 100:
        print('|--------------APROVADO--------------|')
        print(f'Item : {venda()}')
        print(f' Pedido : {codigo} '), Gerenciamento.aprovado()

    elif codigo > 100 and codigo < 500:
        print('|--------------ANALISE---------------|')
        print(f'Pedido : {codigo}')
        Gerenciamento.analise()

    elif codigo > 500 and codigo < 700:
        print('|--------------CANCELADO-------------|')
        print(f'Pedido : {codigo}')
        Gerenciamento.cancelado()
api()

print("|====================================|")
print("|====================================|")
time.sleep(0.5)
def hub():
    print('|--------------HUB COMERCE-----------|')

    def importar():
        if codigo > 1 and codigo < 100:
            print('|--------------IMPORTAR--------------|')
            Gerenciamento.atualizando()
    importar()    

    def atualizar():
        if codigo > 100 and codigo < 500:
            print('|--------------ATUALIZAR-------------|')

            Gerenciamento.atualizar()
    atualizar()

    if codigo > 500 and codigo < 700:
        print('|--------------CANCELAR--------------|')

        Gerenciamento.cancelado()

hub()

def venda():
    pass



        
