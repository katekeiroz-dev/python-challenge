#Desafio07 : Desenvolva um programa que leia as duas
# notas de um aluno. Calcule e mostre a sua media

nota1 = float(input('Digite a sua primeira nota:'))
nota2 = float(input('Digite a sua segunda nota :'))
c = float((nota1+nota2)/2)


print('Sua media e {:.1f}'.format(c))
