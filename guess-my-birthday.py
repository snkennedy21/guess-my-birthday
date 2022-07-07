from calendar import month
import code
from random import randint

# Using a While loop

name = input("Hi! What's your name: ")

max_year = 2004
min_year = 1924

month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


i = 5
while i >= 0:
  year_guess = randint(min_year, max_year)
  month_guess = randint(0, len(month_list))

  if i == 5:
    player_response = input(f'{i} Guesses Remaining: {name} were you born in {month_guess} / {year_guess} (y)es or (n)o: ')

  if player_response.lower() != 'n' and player_response.lower() != 'l':
    print('invalid input')
    player_response = input(f'{i} Guesses Remaining: {name} were you born in {month_guess} / {year_guess} (y)es or (n)o: ')

  if player_response.lower() == 'n':
    i = i - 1
    print('Drat! Let me try again!')
    month_guess = randint(0, len(month_list))
    year_guess = randint(min_year, max_year)
    player_response = input(f'{i} Guesses Remaining: {name} were you born in {month_guess} / {year_guess} (y)es or (n)o: ')

  if player_response.lower() == 'y':
    print('I knew it!')
    break

  if i == 1 and player_response.lower() == 'n' :
    print('I have more important things to do')
    break