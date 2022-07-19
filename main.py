import os


def render(secret_word, user_attempts):
    result = ''
    errors = 0
    for letter in secret_word:
        if letter in user_attempts:
            result += letter
        else:
            result += '_'
    for letter in user_attempts:
        if letter not in secret_word:
            errors += 1
    print('*____________*')
    print('|            |')
    if errors == 0 or len(user_attempts) == 0:
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif errors == 1:
        print('|          (ಠ_ಠ)')
        print('|')
        print('|')
        print('|')
        print('|')
    elif errors == 2:
        print('|          (ಠ_ಠ)')
        print('|            |')
        print('|            |')
        print('|')
        print('|')
    elif errors == 3:
        print('|          (ಠ_ಠ)')
        print('|           /|')
        print('|          / |')
        print('|')
        print('|')
    elif errors == 4:
        print('|          (ಠ_ಠ)')
        print('|           /|\\')
        print('|          / | \\')
        print('|')
        print('|')
    elif errors == 5:
        print('|          (ಠ_ಠ)')
        print('|           /|\\')
        print('|          / | \\')
        print('|           /')
        print('|          /')
    elif errors == 6:
        print('|          (ಠ_ಠ)')
        print('|           /|\\')
        print('|          / | \\')
        print('|           / \\')
        print('|          /   \\')
        print('|', secret_word)
        print('| -- PERDEU, TROUXA!! -- |')
        exit()
    print('*', result)
    if result == secret_word:
        print('| -- FINALMENTE -- |')
        exit()


os.system('clear')
secret = input('MANDA A BRABA: ').upper()
os.system('clear')
while not secret.isalpha():
    os.system('clear')
    secret = input('MANDA A BRABA CERTO, SEU BOSTA!: ').upper()
    os.system('clear')
inputs = []
while True:
    render(secret, inputs)
    attempt = input('TENTA A SORTE, VACILÃO: ').upper()
    if attempt in inputs:
        os.system('clear')
        print('ESSA JÁ FOI, SEU BOCA DE BURRO!')
        continue
    if len(attempt) == 0:
        os.system('clear')
        print('TEM QUE POR UMA LETRA, SUA ANTA!')
        continue
    if not attempt.isalpha():
        os.system('clear')
        print('SÓ TRABALHO COM LETRAS, SUA CENTOPÉIA PARALÍTICA!')
        continue
    if len(attempt) > 1:
        os.system('clear')
        print('UMA LETRA POR VEZ, SEU ANIMAL DE TETA!')
        continue
    inputs.append(attempt)
    os.system('clear')
