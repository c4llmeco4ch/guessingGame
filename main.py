low = 0
high = 100
guess = 50
correct = False

while not correct and high >= low:
  print("My guess is "+ str(guess))
  validAns = False
  while not validAns:
    ans = input("Too high (h), too low (l) or correct (c)?: ")
    if(ans == "c"):
      print("Yay :D")
      exit()
    elif(ans == "h"):
      high = guess - 1
      guess = (high + low) // 2
      validAns = True
    elif(ans == "l"):
      low = guess + 1
      guess = (high + low) // 2
      validAns = True
    else:
      print("This is not a valid input. Try again\n")
print("You've been lying to me >:( \n" +
        "try again when you've made up your mind")
  
  
