print("Welcome to the Quiz!") 
play = input("Do want to play? ")
score = 0
if play.lower() != "yes":
    quit()
else:
    print("Let's start :) ")
answer = input("What is a stack? ")
if answer.lower() == "linear data structure":
    print("correct!")
    score += 1
else:
    print('Incorrect!')
    
answer = input("What is PSU? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print('Incorrect!')
   
answer = input("what is sql? ")
if answer.lower() == "structured query language":
    print("correct!")
    score += 1
else:
    print('Incorrect!')
   
answer = input("what does 26L of the A stand for? ")
if answer.lower() == "26 letters of the alphabet":
    print("correct!")
    score += 1
else:
    print('Incorrect!')
    
print("Your total score is " +str(score))
print("You got "+str((score/4) * 100) +"%")