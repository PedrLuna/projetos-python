#17.	Crie o código para fazer a criação ao dos novos tipos de dados conforme solicitado abaixo:
#a.	Horário: composto de hora, minutos e segundos. ´
#b.	Data: composto de dia, mês e ano. ˆ
#c.	Compromisso: composto de uma data, horário e texto que descreve o compromisso
class Agenda:
    data = None
    horario = None
    descricao = None
    def __init__(self, data, horario, descricao):
        self.data = data
        self.horario = horario
        self.descricao = descricao
lista = []
while True:
    print('\nDigite 0 para finalizar o programa')
    print('\n', '----' * 6)
    data = input('\nDigite a data (formato dia/mês/ano): ')
    print('\n','----'*6)
    if data == '0':
        break
    else:
        horario = input('\nDigite a hora (formato 24 hrs): ')
        print('\n', '----' * 6)
        descricao = input('\nDigite o compromisso: ')
        print('\n', '----' * 6)
        coisa = Agenda(data,horario,descricao)
        lista.append(coisa)
print('\n---------Lista Completa---------')
for x in lista:
    print('\nA data é -->',x.data)
    print('\nO horario é as -->',x.horario)
    print('\nO compromisso é -->',x.descricao)
    print('--------------------------------\n')