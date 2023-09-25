def ask_for_input(word):
    
    while True:
        
        guess=input("Please enter a signle letter: ")
        
        
        if(len(guess)==1 and guess in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"):
            
            break
    
        else:
            
            print("Invalid letter. Please, enter a single alphabetical character.")


    check_guess(word,guess)



def check_guess(word,guess):

    if (guess.lower() in word):

        print(f"Good guess! {guess} is in the word.")

    else:

        print(f"Sorry, {guess} is not in the word. Try again.")   


ask_for_input("apple")

