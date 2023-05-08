#leia um preco de um produto e mostre seu valor com 5% de desconto

pro = float(input('Qual o valor do produto?'))
cal = pro - (pro * 5 / 100)

print('O produto de valor {} com 5% de desconto fica por {} !'.format(pro, cal))