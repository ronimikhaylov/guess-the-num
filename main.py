#Number Guessing Game 
import random
logo = '''____ _  _ ____ ____ ____    ___ _  _ ____    _  _ _  _ _  _ ___  ____ ____   /
| __ |  | |___ [__  [__      |  |__| |___    |\ | |  | |\/| |__] |___ |__/  / 
|__] |__| |___ ___] ___]     |  |  | |___    | \| |__| |  | |__] |___ |  \ .  
                                                                              '''
print(logo)
rand_num = 0
def guess_num():
  global rand_num
  rand_num = random.randint(1,100)
  return rand_num

def check_guess(guess):
  if (rand_num < guess):
    str = "Too high."
  elif(rand_num > guess):
    str = "Too Low."
  elif(rand_num == guess):
    str = "Correct!"
  return str

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if (level == 'easy'):
  numTries = 10
elif(level == 'hard'):
  numTries = 5
countTries = 0
stop = False
guessed_num = guess_num()
user_accuracy = ""
while countTries < numTries and  not stop:
  #print(guessed_num)
  print(f"You have {numTries - countTries} attempts remaining to guess the number.")
  user_guess = int(input("Make a guess: "))
  user_accuracy = check_guess(user_guess)
  print(user_accuracy)
  if user_accuracy == "Correct!":
    stop = True
  
  countTries +=1
if (countTries == numTries and not stop):
  print("Loser")

