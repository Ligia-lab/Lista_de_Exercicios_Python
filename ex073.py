#Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) apenas os 5 primeiros colocados
# B) os ultimos 4 colocados da tabela
# C) uma lista com os times em ordem alfabética
# D) em que posição na tabela está o são paulo

times = ('PALMEIRAS', 'INTERNACIONAL', 'FLUMINENSE', 'CORINTHIANS', 'FLAMENGO',
         'ATHLETICO-PR',	'ATLÉTICO-MG', 'FORTALEZA', 'SÃO PAULO', 'AMÉRICA-MG',
         'BOTAFOGO', 'SANTOS', 'GOIÁS', 'RED BULL BRAGANTINO', 'CORITIBA', 'CUIABÁ',
         'CEARÁ', 'ATLÉTICO-GO', 'AVAÍ', 'JUVENTUDE')
sao_paulo = times.index('SÃO PAULO')

print(f'Os 5 primeiros colocados na tabela são {times[0:5]}.')
print(f'Os 4 times na zona de rebaixamento são {times[-4:]}.')
print(f'A lista dos times em ordem alfabetica é: {sorted(times)}.')
print(f'O São Paulo está na {sao_paulo + 1}ª posição.')
