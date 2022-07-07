import random
import string

# tamanho da senha
tam = int(input("Digite a quantidade de caracteres da senha: "))

while tam < 16:
    print("Atenção, o mínimo de caracteres recomendados é 16.")
    tam = int(input("Digite a quantidade de caracteres da senha: "))

# gera um caractere aleatório entre letras maiusculas e minusculas, digitos e simbolos
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()><:.,'

# função que pega char aleatório
rnd = random.SystemRandom()

# join do char aleatorio com 16 letras
print(''.join(rnd.choice(chars) for i in range(tam)))
