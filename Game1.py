import random
'''
    1 for snake
    2 for water
    3 for gun
              '''
computer = random.choice([1,2,3])
youstring = input("enter your choice : ")
yourdict = {"s": 1,"w":2,"g":3}
reversedict = {1:"snake",2:"water",3:"gun"}
you = yourdict[youstring]
print(f" Your choice : {reversedict[you]}\n computer choice : {reversedict[computer]}")
if(computer == you):
    print("IT IS A DRAW")
else:
    if(you == 1 and computer ==2):
        print("YOU WIN")  
    elif(you ==1 and computer ==3):
        print("YOU LOSE")   
    elif(you == 2 and computer ==1):
        print("YOU LOSE")   
    elif(you == 2 and computer ==3):
        print("YOU WIN")  
    elif(you == 3 and computer == 1):
        print("YOU WIN")    
    elif(you ==3 and computer ==2):
        print("YOU LOSE")
    else:
        print("NO RESULT. SOME ERROR")    
