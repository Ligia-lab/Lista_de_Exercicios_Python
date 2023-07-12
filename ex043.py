# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# Entre 25 e 30: sobrepeso
# Entre 30 e 40: obesidade
# acima de 40: obesidade mórbida

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f}, você está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de {:.1f}, você está no peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.1f}, você está com sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.1f}, você está com obesidade.'.format(imc))
else:
    print('Seu IMC é de {:.1f}, você está com obesidade mórbida.'.format(imc))