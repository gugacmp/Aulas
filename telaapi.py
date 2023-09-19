import tkinter as tk

# Função para atualizar os campos
def atualizar_campos():
    produto = produto_entry.get()
    valor = valor_entry.get()
    quantidade = quantidade_entry.get()
    
    # Aqui você pode adicionar a lógica para atualizar os campos conforme necessário
    # Por enquanto, apenas exibiremos os valores
    resultado_label.config(text=f"Produto: {produto}, Valor: {valor}, Quantidade: {quantidade}")

# Função para importar
def importar_dados():
    # Adicione aqui a lógica para importar dados
    pass

# Função para gravar
def gravar_dados():
    # Adicione aqui a lógica para gravar dados
    pass

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro")
root.geometry("400x500")

# Campos de entrada
produto_label = tk.Label(root, text="Produto:")
produto_label.pack()
produto_entry = tk.Entry(root)
produto_entry.pack()

valor_label = tk.Label(root, text="Valor:")
valor_label.pack()
valor_entry = tk.Entry(root)
valor_entry.pack()

quantidade_label = tk.Label(root, text="Quantidade:")
quantidade_label.pack()
quantidade_entry = tk.Entry(root)
quantidade_entry.pack()

# Botões
atualizar_button = tk.Button(root, text="Atualizar", command=atualizar_campos)
atualizar_button.pack()

importar_button = tk.Button(root, text="Importar", command=importar_dados)
importar_button.pack()

gravar_button = tk.Button(root, text="Gravar", command=gravar_dados)
gravar_button.pack()

# Rótulo para exibir os resultados
resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()
