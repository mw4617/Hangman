import random as rnd

word_list=["blue berry","bananna","raspeberry","pineapple ","mango"]

def user_input():

    guess=input("Please enter a signle letter: ")

    if(len(guess)==1 and guess in "qwertyuiopasdfghjklzxcvbnm"):

        return guess

    else:

        print("Oops! That is not a valid input. Please try again.")    

        return user_input()


guess=user_input()

print(f'The guess is: {guess}')

#for word in word_list:

    #print(word)

def random_choice(list):

    word=rnd.choice(list)

    print(word)


random_choice(word_list)
