import random as rnd


word_list=["blue berry","bananna","raspeberry","pineapple","mango"]

def play_game(word_list):

    num_lives=5

    game = Hangman(word_list,num_lives)

    game.ask_for_input()

    

class Hangman:

    def __init__(self,word_list,num_lives):
        
        self.word_list=word_list

        self.num_lives=num_lives

        self.word=rnd.choice(word_list)

        self.word_guessed=['_' for  x in self.word]

        self.num_letters=len(self.word_guessed) #number of letters that have not been guessed

        self.list_of_guesses=[]

    def check_guess(self,guess):
        
        if (guess.lower() in self.word):
            
            print(f"Good guess! {guess} is in the word.")

            for i in range(0,len(self.word_guessed)):

                if(self.word[i]==guess):

                    self.word_guessed[i]=guess

                    self.num_letters-=1  

            self.display_word()   
        
        else:
            
            self.num_lives-=1

            print(f"Sorry, {guess} is not in the word. Try again.")       

            print(f"You have {self.num_lives} lives left.")

            self.display_word()
    

    def display_word(self):

        for letter in self.word_guessed:

            print(letter)

    def ask_for_input(self):
        
        while True:
            
            guess=input("Please enter a signle letter: ")
            
            if(len(guess)==1 and guess not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "):
                
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            elif(guess in self.list_of_guesses):
                
                print("You already tried that letter")
                
            else:
                
                self.check_guess(guess) 

                self.list_of_guesses.append(guess)  

                if (self.num_lives==0):
                    
                    print("You lost")

                    break

                elif(self.num_letters==0):

                    print("Congratulations You have won the game")    

                    self.display_word()

                    break



play_game(word_list)               