# Desafi08: Escreva um programa que leia u  valor em metro e
#exiba convertido em milimetros.

v = float(input('<<<<Converta metros em milimetros>>> \n Quantos metros :'))
m = float(v * 1000)

print('{}m tem {:.0f}mm'.format(v, m))
