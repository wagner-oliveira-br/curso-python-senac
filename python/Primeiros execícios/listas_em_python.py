idade  = 20
nome = "Wagner"

print (f'O meu nome é {nome} e eu tenho {idade} anos de idade')

lista = [nome, idade]
print (lista)

matriz = [
    ['Sérgio', 29],
    ['Taliny', 22],
    ['Wagner', 20]
]

print ('Mostrando a primeira linha:', matriz[0])
print ('Mostrando a  segunda linha:', matriz[1])
print ('Mostrando o primeiro item da terceira linha:', matriz [2][0])
print ('Mostrando todos as linhas', matriz[0], matriz[1], matriz[2])

lista = ["p", "y", "t", "h", "o", "n"]

print (lista [0:])
print (lista [:2])
print (lista [1:3])
print (lista [0:3:2])
print (lista [-1])