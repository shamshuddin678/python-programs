'''
question:
->Create a display od capable of dispalying questions to the user like KBC.
->Use list data type to store questions and their correct answers.
->Display the final amount of person taking home after playing the game.
'''

# match Questions:
#     case 1:
#         if(reply == question[1]):
#             print(f"Congratulations we owned{levels[1]}")
#     case 2:
#         if(reply == question[2]):
#             print(f"Congratulations we owned{levels[2]}")
#     case 3:
#         if(reply == question[2]):
#             print(f"Congratulations we owned{levels[3]}")
#     case 4:
#         if(reply == question[1]):
#             print(f"Congratulations we owned{levels[4]}")
#     case 5:
#         if(reply == question[3]):
#             print(f"Congratulations we owned{levels[5]}")
#     case 6:
#         if(reply == question[4]):
#             print(f"Congratulations we owned{levels[6]}")
#     case 7:
#         if(reply == question[4]):
#             print(f"Congratulations we owned{levels[7]}")
#     case 8:
#         if(reply == question[4]):
#             print(f"Congratulations we owned{levels[8]}")
#     case 9:
#         print("Wrong answer!")
#         break
# else:
#     print("Wrong answer!")

questions = [
    ["Which car was first invented?", 
     ["Mercedes", "BMW", "Lamborghini", "Ferrari"], 1],

    ["Which is the fastest car among them?", 
     ["Mercedes", "BMW", "Lamborghini", "Ferrari"], 3],

    ["Which country is famous for the sports car brand Porsche?", 
     ["Italy", "Germany", "France", "USA"], 2],

    ["Which company manufactures Ferrari sports cars?", 
     ["Germany", "Italy", "USA", "Japan"], 2],

    ["Which car is known as 'The Prancing Horse'?", 
     ["Lamborghini", "Bugatti", "Ferrari", "McLaren"], 3],

    ["The McLaren F1 used an engine from which company?", 
     ["Ferrari", "Mercedes", "Ford", "BMW"], 4],

    ["What engine layout does the Porsche 911 use?", 
     ["Front V8", "Mid rear V6", "Front-mid flat-six", "Rear-mounted flat-six"], 4],

    ["What does GT stand for in sports cars?", 
     ["Grand Trophy", "Grand Turbine", "Great Turbo", "Grand Touring"], 4]
]

levels = [1000,2000,3000,5000,10000,20000,40000,60000,80000,160000,320000]

money = 0
print(f"Welcome to Kon Banega Carodpathi")
for i in range(len(questions)):
    question = questions[i]

    print("\nQuestion for Rs.", levels[i])
    print(question[0])

    print(f"1. {question[1][0]}")
    print(f"2. {question[1][1]}")
    print(f"3. {question[1][2]}")
    print(f"4. {question[1][3]}")

    reply = int(input("Enter option (1-4): "))

    if i == 0 and reply == 1:
        money = levels[i]
        print(f"Congrats You won RS.{money}")
    elif i == 1 and reply == 2:
        money = levels[i]
        print(f"Congrats You won RS.{money}")
    elif i == 2 and reply == 2:
        money = levels[i]
        print(f"Congrats You won RS.{money}")
    elif i == 3 and reply == 1:
        money = levels[i]
        print(f"Congrats You won RS.{money}")
    elif i == 4 and reply == 3:
        money = levels[i]
        print(f"Congrats You won RS.{money}")
    elif i == 5 and reply == 4:
        money = levels[i]
        print(f"Congrats You won RS.{money}")
    elif i == 6 and reply == 4:
        money = levels[i]
        print(f"Congrats You won RS.{money}")
    elif i == 7 and reply == 4:
        money = levels[i]
        print(f"Congrats You won RS.{money}")
    else:
        print("Wrong Answer!")
        break

print(f"\nYou go to home with Rs. {levels[i-1]}")