'''Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!'''
words={
    "katha":"eat",
    "kapdhe":"clothes",
    "kithab":"book"
}

user=input("Enter your choice of word to know its meaning: ")
print(words[user])