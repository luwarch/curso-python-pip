
import random



computer_wins_score = 0
user_wins_score = 0


# Choice Option Area
def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera: ')
  user_option = user_option.lower()

  if not user_option in options:
    print(user_option + ' no es una opción valida')
    # continue
    return None, None

  computer_option = random.choice(options)

  print('User option : ', user_option)
  print('Computer option : ', computer_option)
  return user_option, computer_option


# Check Rules Area
def check_rules(user_option, computer_option, user_wins_score, computer_wins_score):
  if user_option == computer_option:
    print('empate, ambos eligieron lo mismo')

  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gana')
      user_wins_score += 1
    else:
      print('papel gana a piedra')
      print('computer gana')
      computer_wins_score += 1

  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user ganó')
      user_wins_score += 1
      
    else:
      print('tijera gana a papel')
      print('computer gano')
      computer_wins_score += 1

  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gana')
      user_wins_score += 1
      
    else:
      print('piedra gana a tijera')
      print('computer gana')
      computer_wins_score += 1

  return user_wins_score, computer_wins_score
  

def run_game():
 computer_wins_score =  0
 user_wins_score = 0
 rounds = 1
  

 while True:
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10),

  print('computer_wins', computer_wins_score)
  print('user_wins', user_wins_score)
  rounds += 1  
   

  user_option, computer_option = choose_options()
  user_wins_score, computer_wins_score = check_rules(user_option, computer_option, user_wins_score, computer_wins_score)
  

  
# Printing-VAlidation Area
  if computer_wins_score == 2:
    print('terminó en juego, el ganador es Computer')
    break

  if user_wins_score == 2:
    print('terminó en juego, el ganador es User')
    break

  
run_game()