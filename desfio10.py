#Faca um programa que leia quanto de diheiro vc tem e quanto consegue comprar em dolar e euro.

v = float(input(' Quanto voce tem em R$ ?'))

c = float( v / 4.99)
e = float(v / 5.46)
print('Com R${} voce consegue comprar {:.2f}$'.format(v,c))
print(' e com o mesmo valor em real voce consegue comprar {:.2f}euros'.format(e))