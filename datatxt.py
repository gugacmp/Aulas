import aula5 
# Dados que você deseja salvar em um arquivo de texto
dados = aula5.aprovado

# Nome do arquivo de texto onde os dados serão salvos
nome_arquivo = "aprovado.txt"

# Abre o arquivo para escrita (modo "w" significa escrever)
#with open(nome_arquivo, "w") as arquivo:
#    arquivo.write(dados)

print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'")
