import math
import random


while True:
  number = 0
  
  while True:
    rChoice = random.choice(["sqrt", "half", "+100"])
    if number > 100:
      number -= 50
    if rChoice == "sqrt":
      number = math.sqrt(number)
    elif rChoice == "half":
      number = number/2
    elif rChoice == "+100":
      number += 100
    Rnumber = random.randint(0,10000000)
    if Rnumber >= 9999000:
      break
  print("You will die in", math.floor(number), "years.")
  while True:
    rChoice2 = random.choice(["killed by train", "ran over by car", "car accident", "death.fell.accident.water", "death by toaster being hurled out a b2 bomber which had been towed by a volkswagen mk1 gti then it exploded"])
    Rnumber = random.randint(0,10000000)
    if Rnumber >= 9999000:
      break
  print("Your death cause will be", rChoice2)
  input("Go again?")
