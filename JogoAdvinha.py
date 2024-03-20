import random
import time

numero_comp = random.randint(0, 5)
print('Deixa eu pensar por um segundo....')
time.sleep(2)
print('Tente adivinhar o número que estou pensado!')
time.sleep(1.2)
print("HAHAHAHAHAHAHAHAHAHA")
time.sleep(1.2)
numero_user = int(input('\nDigite um número de 0 a 5: '))
time.sleep(1.4)
if numero_user == numero_comp:
    print('Parabéns!! Você acertou o número que eu pensei')
else:
    print('Você errou! Que tempo perdido...')
    print(f'Eu pensei no número: {numero_comp}')