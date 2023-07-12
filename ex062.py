#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão desejada: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Mostrar mais quantos termos  : '))
print('PA finalizada com {} termos mostrados.'.format(total))
print('FIM')
