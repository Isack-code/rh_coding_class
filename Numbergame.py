import argparse
import random
import time
## test
parser = argparse.ArgumentParser(
                    prog='Numbergame.py',
                    description='A number guessing game',
                    epilog='This game was made by Isaac Payne')
parser.add_argument('--max_number', type=int, help='Guess between 1 and max number', default=10)


def get_number_from_user(max_number):
    number = int(input(f"Please enter a number between 1 and {max_number} "))
    return number

def create_number(max_number) -> int:
    return random.randint(1, max_number)

def define_difference(usernumber, creatednumber):
    return abs(usernumber - creatednumber)

def display_results(user_number, created_number, difference):
  print(f"Created Number: {created_number}, Your Guess: {user_number}, Difference: {difference}")

if __name__ == "__main__":
  args = parser.parse_args()
  usernumber = get_number_from_user(args.max_number)
  creatednumber = create_number(args.max_number)
  difference = define_difference(usernumber, creatednumber)
  if difference == 0:
      print("You got it right!")
      display_results(usernumber, creatednumber, difference)
  else:
      for retry in range(3):
          if usernumber > creatednumber:
              print("You were too high")
          else:
              print("You were too low")
          usernumber = get_number_from_user(args.max_number)
          difference = define_difference(usernumber, creatednumber)
          if difference == 0:
              print("You got it right!")
              break
      display_results(usernumber, creatednumber, difference)

