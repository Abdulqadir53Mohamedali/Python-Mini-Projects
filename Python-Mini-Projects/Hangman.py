#secret_word = input('Please type in a word for your friend to choose:').lower()
secret_word = 'word'
lettercount = ""
failed_count = 6

def hangman():
    print('No capital letter are included within the secret word')
    print("""""""""""""")
    failed_count = 6
    while failed_count > 0:
        guess = input('Enter a letter:')
        if guess in secret_word:
            print(f'Correct!, there is one or more {guess} in the secret word')
        else:
            failed_count -= 1
            print(f'Incorrect! The letter {guess} is not in the secret word')
            
        lettercount += guess
        wrong_letter_count = 0
        
        for letter in secret_word:
            if letter in lettercount:
                print(f"{letter}", end="")
            else:
                print("_", end="",)
                wrong_letter_count += 1
                
        if wrong_letter_count == 0:
            print(f"\nCongratulations!, the secret word was: {secret_word}, you won ")
            break
    else:
        print("\nYou did not win this time, unlucky")
        print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
        hangman()

hangman()
