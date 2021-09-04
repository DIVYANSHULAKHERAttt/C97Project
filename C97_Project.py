number = input("Guess what my number between 1 and 9 is!")
while number != 5: 
    if 1 < float(number) < 5:
        print(number + "? Guess higher!")
        number = input("Guess another number!")
    elif 10 > float(number) > 5:
        print ("? Guess lower!")
        number = input("Guess another number!")
    elif float(number) <= 0 or float(number) >= 9:
        print ("? Hey, I said guess a number between 1 to 9")
        number = input("Guess another number!")
    if float(number) == 5:
        print(number + "Congrats! You won the game!")
        break
    
