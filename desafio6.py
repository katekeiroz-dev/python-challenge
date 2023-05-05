# Desafio 06 : Crie um algoritimo que leia um numero e mostre o seu dobre , triplo e raiz quadrada

n = int(input('Digite um numero que seja inteiro:'))
d = int(n*2)
t = int(n*3)
r = float(n**(1/2))

print('O numero {} tem o dobro de {} , o triplo {} e a raiz quadrada {:.2f}'.format(n, d, t, r))

