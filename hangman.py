# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
def warning_cause(userinput,warning):
    if warning<0:
        warning=0
    if len(userinput)!=1:
        return "Oops! Enter only one letter.\nYou have {} warnings left".format(warning)
    elif (not userinput.isalpha()):
        return "Oops! You have to input alphabets only.\nYou have {} warnings left".format(warning)
    else:
        return "Oops! You've already guessed that letter. You now have {} warnings".format(warning)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    n=len(secret_word)
    i=0
    result=True
    while i<n and result:
        result=secret_word[i] in letters_guessed
        i+=1
    return result
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    n=len(secret_word)
    i=0
    s=""
    while i<n:
        if secret_word[i] in letters_guessed:
            s+=secret_word[i]
        else:
            s+=" _ "
        i+=1
    return s


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alpha=string.ascii_lowercase
    s=""
    l=list(alpha)
    for i in letters_guessed:
        l.remove(i)
    return s.join(l)
    
    

def hangman(secret_word):
    print("Welcome to the game Hangman!")
    n=len(secret_word)
    print("I am thinking of a word that is {} letters long.".format(n))
    print("_ "*n)
    guesses=6
    letters_guessed=[]
    warning=3
    while not (guesses==0 or  is_word_guessed(secret_word, letters_guessed)):
        print("You have {} guesses left.".format(guesses))
        print("\nAvailable letters: {}".format(get_available_letters(letters_guessed)))
        userinput=(input("Please guess a letter: ")).strip()
        while len(userinput)!=1 or (not userinput.isalpha()) or (not (userinput in get_available_letters(letters_guessed))):
            print("_ _ _ _ _ _ _ _ _ _ ")
            warning-=1
            if warning>=0:
                print(warning_cause(userinput,warning))
                print("You have {} guesses left.".format(guesses))
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                print(warning_cause(userinput,warning))
                print("As you were warned before you lose one guess")
                guesses-=1
                print(get_guessed_word(secret_word, letters_guessed))
                if guesses==0:
                    break
                print("You have {} guesses left.".format(guesses))
            print("\nAvailable letters: {}".format(get_available_letters(letters_guessed)))
            userinput=(input("Please guess a letter: ")).strip()
        if guesses<=0:
            break
        userinput=userinput.lower()
        letters_guessed+=[userinput]
        if userinput in secret_word:
            print("\nGood guess: {}".format(get_guessed_word(secret_word, letters_guessed)))
        else:
            print("\nOops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
            guesses-=1
            if userinput in ["a","e","i","o","u"]:
                guesses-=1
        print("\n_ _ _ _ _ _ _ _ _ _ ")
    if guesses==0:
        print("\nSorry, you ran out of guesses.")
        print("The word was: {}".format(secret_word))
    elif is_word_guessed(secret_word, letters_guessed):
        print("\nCongratulations, you won!")
        sets="".join(set(secret_word))
        print("Your total score for this game is: {}".format(guesses*len(sets)))
    
    
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    myword=my_word.replace(" ","")
    splited=list(myword)
    n=len(splited)
    if n!=len(other_word):
        return False
    for i in range(n):
        if splited[i].isalpha():
            if splited[i]!=other_word[i]:
                return False
        else:
            if other_word[i] in splited:
                return False
    return True


def show_possible_matches(my_word):
    reveled=False
    for i in wordlist:
        if match_with_gaps(my_word,i):
            print(i+" ",end="")
            reveled=True
    print()
    if not reveled:
        print("No matches found")



def hangman_with_hints(secret_word):
    print("Welcome to the game Hangman!")
    print("Here Are Rules For Your Game") 
    print()
    print("press enter to view next line")
    n=len(secret_word)
    for i in range(1,len(rules)):
        input()
        print(rules[i])
    print("I am thinking of a word that is {} letters long.".format(n))
    print("_ "*n)
    guesses=6
    letters_guessed=[]
    warning=3
    while not (guesses==0 or  is_word_guessed(secret_word, letters_guessed)):
        print("You have {} guesses left.".format(guesses))
        print("\nAvailable letters: {}".format(get_available_letters(letters_guessed)))
        print(get_guessed_word(secret_word, letters_guessed))
        userinput=(input("Please guess a letter: ")).strip()
        if userinput=="*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        while len(userinput)!=1 or (not userinput.isalpha()) or (not (userinput in get_available_letters(letters_guessed))):
            print("_ _ _ _ _ _ _ _ _ _ ")
            warning-=1
            if warning>=0:
                print(warning_cause(userinput,warning))
                print("You have {} guesses left.".format(guesses))
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                print(warning_cause(userinput,warning))
                print("As you were warned before you lose one guess")
                guesses-=1
                print(get_guessed_word(secret_word, letters_guessed))
                if guesses==0:
                    break
                print("You have {} guesses left.".format(guesses))
            print("\nAvailable letters: {}".format(get_available_letters(letters_guessed)))
            userinput=(input("Please guess a letter: ")).strip()
            if userinput=="*":
                break
        if userinput=="*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        if guesses<=0:
            break
        userinput=userinput.lower()
        letters_guessed+=[userinput]
        if userinput in secret_word:
            print("\nGood guess: {}".format(get_guessed_word(secret_word, letters_guessed)))
        else:
            print("\nOops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
            guesses-=1
            if userinput in ["a","e","i","o","u"]:
                guesses-=1
        print("\n_ _ _ _ _ _ _ _ _ _ ")
    if guesses==0:
        print("\nSorry, you ran out of guesses.")
        print("The word was: {}".format(secret_word))
    elif is_word_guessed(secret_word, letters_guessed):
        print("\nCongratulations, you won!")
        sets="".join(set(secret_word))
        print("Your total score for this game is: {}".format(guesses*len(sets)))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

#     To test part 2, comment out the pass line above and
#     uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    fin=open("rules.txt","r")
    rules=fin.readlines()
    fin.close()  
    hangman_with_hints(secret_word)
