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