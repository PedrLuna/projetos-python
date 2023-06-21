import time
import math
lista = []
print('''PRODUTORIO ROBÔ
    ╲┈┈┈┈╱
    ╱    ╲ 
   ┃┈▇┈┈▇┈┃
 ╭╮┣━━━━━━┫╭╮
 ┃┃┃┈┈┈┈┈┈┃┃┃
 ╰╯┃┈┈┈┈┈┈┃╰╯
   ╰┓┏━━┓┏╯
    ╰╯  ╰╯''')
time.sleep(2)
print('Inicializando espere.')
print('[                   ]')
time.sleep(0.8)
print('[█████              ]')
time.sleep(0.8)
print('[██████████         ]')
time.sleep(0.8)
print('[███████████████████]')
def calculo(x, y, i):
    i = 1
    while i <= x:
        aux = (i * y)
        print(aux, '.', end=(' '))
        i += 1
        lista.append(aux)
while True:
    print('\n\nSe quiser sair digite 0 em todos\n\n')
    x = int(input('DIGITE O VALOR DE X: '))
    y = int(input('\nDIGITE O VALOR DE y: '))
    i = int(input('\nDIGITE O VALOR DE i: '))
    if x == 0 and y == 0 and i == 0:
        print('''   ROBÔ DESLIGANDO   
         ╲┈┈┈┈╱
         ╱    ╲ 
        ┃┈▇┈┈▇┈┃
      ╭╮┣━━━━━━┫╭╮
      ┃┃┃┈┈┈┈┈┈┃┃┃
      ╰╯┃┈┈┈┈┈┈┃╰╯
        ╰┓┏━━┓┏╯
         ╰╯  ╰╯''')
        time.sleep(1)
        print('[                   ]')
        time.sleep(0.8)
        print('[█████              ]')
        time.sleep(0.8)
        print('[██████████         ]')
        time.sleep(0.8)
        print('[███████████████████]')
        print('	\033[1;31mdevil.exe off\033[0;0m')
        break
    elif x>=0 or x<=0 or y>=0 or y<=0 or i>=0 or i<=0:
        calculo(x, y, i)
        print('\nLista completa:', lista)
        print('Produtorio:', math.prod(lista))