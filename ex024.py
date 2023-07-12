#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

cidade = str(input('Qual cidade você mora? ')).strip()
#print(cidade[:5].title() == 'Santo')
cidade = cidade.title().split()
print('Santo' in cidade[0])
