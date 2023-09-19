import random

numeros = [x*random.randint(1,5)  for x in  range(10)]
numero = [x*random.randint(5,10)  for x in  range(15)]
numer = [x*random.randint(10,15)  for x in  range(20)]

print(f'Lista 1 : {numeros} | Lista 2 : {numero} | Lista 3 : {numer}')

print(f'Primeira Lista :{numeros[4]}') 
print(f'Segunda Lista : {numero[8]}')
print(f'Terceira Lista :{numer[12]}')



