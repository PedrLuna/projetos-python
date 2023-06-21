#Professor essa n soube resolver mas ta aqui minha linha de pensamento em questão dela
print('---'*5, "Fibonacci", '---'*5)
n = int(input(" Até que número você deseja :"))
x = 1
def funcao (n, x):
    if x<=n:
        ex1 = 0
        ex2 = 1
        ex3 = 1
        ex3 = ex1 + ex2
        ex1 = ex2
        ex2 = ex3
        funcao(n, x+1)
        print("{}° termo: {}".format(x, ex3))
    else:
        print('---' * 5, "ACABOU!!!", '---' * 5)
funcao(n,x)