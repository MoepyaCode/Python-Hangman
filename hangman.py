import random, sys


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    ''' 
    1. We should replace characters with underscores.
    2. And also get the random letter here.
    3. Basically word with underscores
    
    '''
    
    wordLength = len(word)  # Length of the word
    randomWordIndex = random.randint(0, wordLength - 1) # The random index from
    randomLetter = word[randomWordIndex]    # Selects the random letter from word
    underscore = '_'
    underscoredWord = ''
    
    for i in range(wordLength):
        
        if word[i] != randomLetter or word[i] == randomLetter and i != randomWordIndex:
            underscoredWord += underscore # 1. Enters under score in place of non-randomLetter letters.
                                          # 2. Condition also checks for actual position.
        
        else:
            underscoredWord += str(randomLetter)    # Enters random letter in string.
        
    return underscoredWord


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    ''' 
    1. Do validation to check if the orginial word contains the user input.
    2. original Word is the full word chosen from list.
    3. Answer word is the one with undescores including word.
    4. Char will be the input character that the user inputs.
        
    '''
    randomLetterIndex = 0 # Declare randomLetterIndex to avoid declaration error.
    
    for i in range(len(answer_word)):
        
        if answer_word[i] != '_':   # 1. If answer word != to underscore.
            randomLetterIndex = answer_word.find(answer_word[i])    # 2. Finds index of random letter in underscored word
    
          
    similarLetterCount = original_word.count(original_word[randomLetterIndex]) # 3. Counts similar letters in word
    randomLetter = original_word[randomLetterIndex]
    
    if char == randomLetter and similarLetterCount == 1: # 4. Returns FALSE because word is given
        return False
    
    elif char == randomLetter and similarLetterCount > 1:# 5. Returns TRUE because there is more than one similar letter in word.
        return char # Therefore, accepts the letter.
            
    elif char in original_word and similarLetterCount == 1 or char in original_word and similarLetterCount > 1:
        return char # 6. Condition looks at other letters that are != to random letter.


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    ''' 
    1. With result of char we replace the underscore in answer word with char.
        Specifically after validation of orginal word.
    2. After the user input we return the answer word.
    '''
    randomWordIndex = 0
    wordLength = len(original_word)
    
    for i in range(wordLength):
        
        if answer_word[i] != '_':   # 1. If answer word != to underscore.
            randomWordIndex = answer_word.find(answer_word[i]) # 2. Finds index of random letter in underscored word
          
    similarLetterCount = original_word.count(original_word[randomWordIndex]) # 3. Counts similar letters in word
    randomLetter = original_word[randomWordIndex]
    answer_word = list(answer_word) # 4. Putting the underscored word in a list.
    
    for i in range(wordLength): # Loops through the word.
            
            if char == original_word[i]: # 5. If char in original word.
                answer_word[i] = char    # 6. The answer_word list is updated and index = the char.
                
    answer_word = ''.join(answer_word) # 7. We now join the word and is no longer an array.
    
    return answer_word # 8. Returns string answer_word.


def do_correct_answer(original_word, answer, guess):
    # Do not change.
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    ''' 
    1. Each time user gets the guess wrong it decreases the chances by 1.
    '''
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    
    
    
    if number_guesses == 0:
        print(''' 
/----
|   0
|  /|\\
|   |
|  / \\
_______ 
''')
        
    elif number_guesses == 1:
        print(''' 
/----
|   0
|  /|\\
|   |
|  
_______ 
''')
    
    elif number_guesses == 2:
        print(''' 
/----
|   0
|   |
|   |
|  
_______ 
''')
        
    elif number_guesses == 3:
        print(''' 
/----
|   0
|   
|   
|  
_______ 
''')
    elif number_guesses == 4:
        print(''' 
/----
|
|
|
|
_______ 
''')
        

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    guess = ''  # 1. Declare as string and now call function in order to call function inside loop.
    numberOfGuesses = 4 
    underscore = '_'
    
    while underscore in answer and numberOfGuesses > -1:
        
        guess = get_user_input().lower() # 2. We call the get_user_input function here.
        
        if guess == '':
            do_wrong_answer(answer, numberOfGuesses)
            numberOfGuesses = numberOfGuesses - 1   # 3. Decrement number of guesses if user enters an empty string.
            
            if numberOfGuesses < 0: # 4. Print this as number of guess have run out.
                print(f'Sorry, you are out of guesses. The word was: {word}')
        
        elif guess == 'exit' or guess == 'quit':
            print('Bye!')
            break
        
        elif is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
            
        else:
            do_wrong_answer(answer, numberOfGuesses)
            numberOfGuesses = numberOfGuesses - 1   # 3. Decrement number of guesses if user enters an empty string.
            
            if numberOfGuesses < 0: # 4. Print this as number of guess have run out.
                print(f'Sorry, you are out of guesses. The word was: {word}') 
        

# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    
    # 1. Allows you to call files that have been created in same folder that are .txt.
    if len(sys.argv) > 1:
        words_file = sys.argv[1]
    else:
        words_file = 'short_words.txt'
        
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)
    
    run_game_loop(selected_word, current_answer)
    
    
