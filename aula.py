import tkinter as tk

def janela():
    root = tk.Tk()
    root.title('Janela')

    def venda(a, b):
        resultado = (a + b)
        valor = float(input('Digite o valor do item : '))
        quantidade = int(input('Digite a quantidade : '))

        soma = resultado(valor, quantidade)
        if valor >  150:
            x = float(valor / 0.5)
        if valor > 200:
            y = float(valor / 1.0)
        else:
            print('Total :', soma)
            
            return resultado 
    root.mainloop()
    venda()
janela()
