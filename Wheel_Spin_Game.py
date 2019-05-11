import random

roll = input("Press Enter to Spin the Wheel or Type Stop " ).lower()
prize = random.randint(0, 100)
print("You're number is " + str(prize) + "!")
while roll != " ":
   roll = input("Press Enter to Spin the Wheel or Type Stop " )
   if (roll == "stop"):
      print("Thank you for playing")
      break
   prize = random.randint(0, 100)
   print("You're number is " + str(prize) + "!")
   if prize < 50:
      print("Sorry, you didn't win. Try again")
   if prize > 50:
      print("Congratulations! You're a winner!")




