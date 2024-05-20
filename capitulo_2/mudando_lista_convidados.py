convidados = ['carlos', 'gustavo', 'lilian']
convidados2 = ['sandro', 'arthur', 'guilherme']
nao_convidados = convidados.pop(1)
convidados.insert(1, 'leticia')

print(f'Você foi convidado para um jantar, {convidados[0].title()}')
print(f'Você foi convidado para um jantar, {convidados[-1].title()}')
print(f'O convidado {nao_convidados.title()} não podera comparecer.')
print(f'Você foi convidado no lugar de {nao_convidados.title()}, {convidados[1].title()}.')
print(f'Você foi convidado para um jantar, {convidados2[0].title()}')
print(f'Você foi convidado para um jantar, {convidados2[1].title()}')
print(f'Você foi convidado para um jantar, {convidados2[-1].title()}')