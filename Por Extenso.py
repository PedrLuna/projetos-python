def numeros(n):
    dc = {
        0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
        16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
        30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
        80: 'oitenta', 90: 'noventa'}
    if n > 99 or n < 0:
        print("O número deve estar entre 0 e 99")

    if n < 20 or n % 10 == 0:
        return dc.get(n)

    decimal = n // 10 * 10
    unidade = n % 10
    extenso = print("{} e {} ".format(dc.get(decimal),dc.get(unidade)))
    return extenso
x = int(input("Digite um número entre 0 e 99: "))
y = numeros(x)
print(y)