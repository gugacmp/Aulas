class Carro:
    def __init__(self, marca, cor, combustivel, portas, ar, preco):
        self.marca = marca = input('Digite a Marca : ')
        self.cor = cor = input('Digite as cores :')
        self.combustivel = combustivel = input('Tipo de combustivel :')
        self.portas =  portas = input('Portas : ')
        self.ar = ar = input('Possui ar condicional ?')
        self.preco = preco = int(input('Informe o valor : '))
        
veiculo = Carro('Ferrari', 'Vermelho', 'Gasolina', '2 Portas', 'S',' ')
veiculo2 = Carro('Lamborguini', 'Azul', 'Nitro', '2 Portas', 'S', ' ')

print('------------------------------------')
print('Primeiro Veiculo')
print(f'Marca :', veiculo.marca)
print(f'Cor :', veiculo.cor)
print(f'Combustivel :', veiculo.combustivel)
print(f'Entradas :', veiculo.portas)
print(f'Ar condicionado :', veiculo.ar)
print('------------------------------------')
print('Segundo Veiculo')
print(f'Marca :', veiculo2.marca)
print(f'Cor :', veiculo2.cor)
print(f'Combustivel :', veiculo2.combustivel)
print(f'Entradas :', veiculo2.portas)
print(f'Ar condicionado :', veiculo2.ar)

if preco > 5000 and ar == 'Sim':
    print(f'Marca {marca} Vendida !')
else:
    print(f'Valor insuficiente para marca:{marca} ser vendida !')