from calendar import month
import code
from random import randint

# Using a While loop

name = input("Hi! What's your name: ")

max_year = 2004
min_year = 1924

month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


i = 5
while i >= 2:
  year_guess = randint(min_year, max_year)
  month_guess = month_list[randint(0, len(month_list) - 1)]

  if i == 5:
    player_response = input(f'\n{i} Guesses Remaining: {name} were you born in {month_guess} / {year_guess}\n(y)es or (n)o: ')

  if player_response.lower() != 'n' and player_response.lower() != 'l':
    print('invalid input')
    player_response = input(f'\n{i} Guesses Remaining: {name} were you born in {month_guess} / {year_guess}\n(y)es or (n)o: ')

  if player_response.lower() == 'n':
    i = i - 1
    print('Drat! Let me try again!')
    month_guess = month_list[randint(0, len(month_list))]
    year_guess = randint(min_year, max_year)
    player_response = input(f'\n{i} Guesses Remaining: {name} were you born in {month_guess} / {year_guess}\n(y)es or (n)o: ')

  if player_response.lower() == 'y':
    print('\nI knew it!')
    break

  if i == 1 and player_response.lower() == 'n' :
    print('\nI have more important things to do')