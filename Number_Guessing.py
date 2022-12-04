import random
nom = input("Enter a number: ")

if nom.isdigit():
    nom = int(nom)
    if nom < 0 :

        print("Please enter a number above 0 next time")
        quit()
else:
    print("Enter a number next time.")
ran = random.randint(0, nom)
score = 0
while True:
    user = input("make a guess: ")
    if user.isdigit():
     user = int(user)
    
    else:
     print("Enter a number next time.")
    
    if user == ran:
        print("You got it!")
        print("you did it in",score, "guesses")
        break
    else:
        print("Try again!")
        score += 1
        if user < ran:
            print("Enter number having range more.")
        else:
            print("Enter number having range less. ")
        continue




