import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print('*' * 10)
    print('Round', rounds)
    print('*' * 10)
    
    print('Computer', computer_wins)
    print('User', user_wins)
    
    user_option = input('piedra, papel o tijera?')
    user_option = user_option.lower()

    if not user_option in options:
        print('Esa opción no es valida')
        continue

    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('¡Ganaste!')
            user_wins += 1
        else:
            print('Papele gana a la piedra')
            print('¡Perdiste!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('¡Ganaste!')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('¡Perdiste!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('¡Ganaste!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('¡Perdiste!')
            computer_wins += 1
    
    if computer_wins == 2:
        print('La computadora es la ganadora')
        break
    
    if user_wins == 2:
        print('Eres el ganador!!')
        break
    
    rounds += 1
