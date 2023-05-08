#faca um programa que leia a altura e largura de uma parede em metros
#calcule a sua area e quantidade de tinta necessaria para pinta-la.
#sabendo que cada litro de tinta pinta uma area de 2m2( dois metros quadrado)

alt = float(input('Qual a altura da parede?'))
larg = float(input('e qual a largura?'))
c = alt * larg
litros = c / 2

print('Uma parede com {} de altural e {} de largura tem uma dimisao de  {}m2. \n para pintar a parede '
      'voce precisara de {}l de tinta'.format(alt, larg, c, litros))


