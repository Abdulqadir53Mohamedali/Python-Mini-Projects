# Initializing the secret word that the user has to guess
secret_word = 'word'
# To keep track of letters guessed by the user
lettercount = ""
# Number of incorrect attempts left
failed_count = 6

def hangman():
    # Informing the user about the format of the secret word
    print('No capital letter are included within the secret word')
    # Printing a separator for visual clarity
    print("""""""""""""")
    # Resetting the failed count for each game
    failed_count = 6
    
    # While loop continues as long as there are attempts left
    while failed_count > 0:
        # Asking user for their letter guess
        guess = input('Enter a letter:')
        
        # Checking if guessed letter is in the secret word
        if guess in secret_word:
            print(f'Correct!, there is one or more {guess} in the secret word')
        else:
            # If the guess is incorrect, decrementing the failed attempts count
            failed_count -= 1
            print(f'Incorrect! The letter {guess} is not in the secret word')
            
        # Adding guessed letter to lettercount to track user's guesses
        lettercount += guess
        wrong_letter_count = 0
        
        # Displaying the current status of the word being guessed
        for letter in secret_word:
            if letter in lettercount:
                print(f"{letter}", end="")
            else:
                # If the letter hasn't been guessed yet, printing an underscore
                print("_", end="",)
                wrong_letter_count += 1
                
        # Checking if the user has guessed the word correctly
        if wrong_letter_count == 0:
            print(f"\nCongratulations!, the secret word was: {secret_word}, you won ")
            break
    # This block executes if the user runs out of attempts
    else:
        print("\nYou did not win this time, unlucky")
        print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
        # Starting a new game
        hangman()

# Starting the game
hangman()
