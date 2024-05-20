convidados = ['carlos', 'gustavo', 'lilian']
nao_convidados = convidados.pop(1)
convidados.insert(1, 'leticia')
convidados.append('guilherme')
convidados.append('arthur')

print(f'Você foi convidado para um jantar, {convidados[0].title()}')
print(f'Você foi convidado para um jantar, {convidados[-1].title()}')
print(f'O convidado {nao_convidados.title()} não podera comparecer.')
print(f'Você foi convidado no lugar de {nao_convidados.title()}, {convidados[1].title()}.')
print(f'Você foi convidado para um jantar, {convidados[3].title()}')
print(f'Você foi convidado para um jantar, {convidados[4].title()}')
print(f'Foi encontrado uma mesa maior {convidados[0].title()}, {convidados[1].title()}, '
      f'{convidados[2].title()}, {convidados[3].title()} e {convidados[4].title()}!')

convidados.insert(0, 'bia')
convidados.insert(3, 'gabriel')
convidados.append('thiago')

print(f'Você foi convidado para um jantar, {convidados[0].title()}')
print(f'Você foi convidado para um jantar, {convidados[3].title()}')
print(f'Você foi convidado para um jantar, {convidados[-1].title()}')
print('A mesa não chegara a tempo e o limite de convidados mudou para 2.')

nao_convidados = convidados.pop(0)
print(f'Lamento, mas o limite de convidados foi excedido, {nao_convidados}')
nao_convidados = convidados.pop(2)
print(f'Lamento, mas o limite de convidados foi excedido, {nao_convidados}')
nao_convidados = convidados.pop(3)
print(f'Lamento, mas o limite de convidados foi excedido, {nao_convidados}')
nao_convidados = convidados.pop(0)
print(f'Lamento, mas o limite de convidados foi excedido, {nao_convidados}')
nao_convidados = convidados.pop(1)
print(f'Lamento, mas o limite de convidados foi excedido, {nao_convidados}')
nao_convidados = convidados.pop(2)
print(f'Lamento, mas o limite de convidados foi excedido, {nao_convidados}')

print(f'Você ainda esta convidado(a), {convidados[0].title()}')
print(f'Você ainda esta convidado(a), {convidados[1].title()}')

del convidados[0]
del convidados[0]
print(convidados)
