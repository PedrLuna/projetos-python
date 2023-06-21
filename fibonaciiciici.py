print('---'*5, "Fibonacci", '---'*5)

n = int(input(" Até que número você deseja :"))
ex1 = 0
ex2 = 1
ex3 = 1
x = 1

while ex3 <= n:
    print("{}° termo: {}".format(x, ex3))
    ex3 = ex1 + ex2
    ex1 = ex2
    ex2 = ex3
    x = x + 1

print('---'*5, "ACABOU!!!", '---'*5)