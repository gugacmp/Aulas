import time
import datetime
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


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
        print(f'Item : {item} | Valor : {valor} | Quantidade : {quantidade}')
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
            time.sleep(0.7)
            now = datetime.datetime.now()
            print(f'Atualizado : {now}')
    atualizar()

    if codigo > 500 and codigo < 700:
        print('|--------------CANCELAR--------------|')

        Gerenciamento.cancelado()

hub()
time.sleep(1)
def aprovado():
    total = valor * quantidade
    rastreio = random.randint(150000,450000)
    chave = random.randint(10000000000000000000000000000000000000000000,90000000000000000000000000000000000000000000)
    now = datetime.datetime.now()

    if codigo == codigo:
        print(f'Emitindo a Venda : {codigo} | Código Rastreio : {rastreio}')
        print(F'ValoR Total : {total}')
        time.sleep(1.5)
        print(f'Venda : {codigo} Autorizada | Chave de acesso : {chave}')
        time.sleep(0.8)
        print(f'Data/Hora da Autorização : {now}')
        time.sleep(0.5)

aprovado()


def gerar_pdf( aprovado):
    c = canvas.Canvas(aprovado, pagesize=letter)
    largura_pagina, altura_pagina = letter

    # Adicione texto ao PDF
    c.drawString(100, altura_pagina - 100, "Exemplo de PDF com ReportLab")
    c.drawString(100, altura_pagina - 120, "Texto adicional aqui.")

    # Desenhe uma forma
    c.rect(100, altura_pagina - 200, 200, 50, stroke=1, fill=0)
    aprovado
    

    # Fecha o PDF
    c.save()

if __name__ == "__main__":
    aprovado = "Api.pdf"
    gerar_pdf(aprovado=aprovado)
    print(f"PDF '{aprovado}' gerado com sucesso!")
