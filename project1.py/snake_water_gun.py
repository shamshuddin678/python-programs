import random

'''
1=snake
-1=water
0=gun
'''
computer=random.choice([1,0,-1])
youstr=input("Enter your choice: ")
you_dict={'s':1,'w':-1,'g':0}
reverse_dict={1:'snake 🐍',-1:'water 🌊',0:'gun 🔫'}
you=you_dict[youstr]
print(f"you choose {reverse_dict[you]}\ncomputer choose {reverse_dict[computer]}")

if(computer == you):
    print("Tie between you and computer")
else:
    if(computer == -1 and you == 1):
        print("you win 🎉🎊")
    elif(computer == -1 and you == 0):
        print("computer win .you lose😒")
    elif(computer == 1 and you == -1):
        print("computer win .you lose😒")
    elif(computer == 1 and you == 0):
        print("you win 🎉🎊")
    elif(computer == 0 and you == 1):
        print("computer win .you lose😒")
    elif(computer == 0 and you == -1):
        print("you win 🎉🎊")
    else:
        print("Something went wrong")                