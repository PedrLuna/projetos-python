#18.	Defina uma estrutura que irá representar bandas de música. Essa estrutura deve ter o nome da banda,
#que tipo de música ela toca,
#o número de integrantes e em que posição do ranking essa banda está dentre as suas 5 bandas favoritas.
class Bandas:
    banda = None
    tipo = None
    nin = None
    posicao = None
    def __init__(self, banda, tipo, nin, posicao):
        self.banda = banda
        self.tipo = tipo
        self.nin = nin
        self.posicao = posicao
x=1
lista=[]
u = 1
while x<=3:
    print('-------------BANDAS DE MUSICAS-------------')
    banda = input('\nQual nome da banda ? ')
    tipo = input('\nQue tipo de musicas eles tocam ? ')
    nin = int(input('\nNúmero de integrantes ? '))
    posicao = int(input('\nEntre suas 5 bandas favoritas essa ocupa a posição ? '))
    bandinha = Bandas(banda,tipo,nin,posicao)
    lista.append(bandinha)
    x= x + 1

print('\n----------------Ranking----------------\n')
for x in lista:
    print('''-=-=-=-=-=-=-=- {}° Lugar -=-=-=-=-=-=-=-=-
        
    Nome da banda: {}
    Tipo de musica: {}
    Número de integrantes: {}
    \n'''.format(x.posicao,x.banda,x.tipo,x.nin))