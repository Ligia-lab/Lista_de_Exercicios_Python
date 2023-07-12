#Refaça o ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('\033[31m-=' * 20)
print('\033[mTABUADAAAAA')
print('\033[31m-=' * 20)

n = int(input('\033[mTabuada do '))

for c in range(1,11):
    print('{} x {} = {}'.format(n, c, c * n))