from random import randint

def game():
    print("You are playing the game...")
    score = randint(1,50)
    with open("files/pratice_set/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):  
            hiscore = int(hiscore) # If score is present it is string we have to convert it into integer 
        else:
            hiscore = 0 # If the file is empty
    print(f"Your score is {score} ")
    if(score > hiscore):
        # Write this hiscore to file
        with open("files/pratice_set/hiscore.txt","w") as f:
            f.write(str(score))
    
    return score

game()    