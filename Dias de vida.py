#6.	Crie uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.
#a.	(suponha anos sempre de 365 dias e meses sempre com 30 dias)
def funcao(a,m,d):
    anos = 365 * a
    meses = 30 * m
    dias = d
    total = anos+meses+dias
    print('O total de dias que você viveu é de {} dias'.format(total))
a = int(input("Anos: "))
m = int(input('Meses: '))
d = int(input("Dias: "))
funcao(a, m, d)
