import random
def choose_word():
    '''
        Randomly choose a word from a list
    '''
    
    with open('./frutas.txt', 'r') as file: #abre o arquivo já existente
        fruits = file.read().split('\n') #lê o conteúdo do arquivo e o salva na variável        
        
    while '' in fruits:
        fruits.remove('')

    n = random.randrange(len(fruits))

    return fruits[n]

def gallows_list():
    gallows = [ 
    """
    |-------
    |      |
    |    
    |    
    |    
    |     
    |     
 ___|___ 
    """,
    
    """
    |-------
    |      |
    |      _
    |     |_|
    |      
    |     
    |     
 ___|___ 
    """,
    """
    |-------
    |      |
    |      _
    |     |_|
    |      |
    |      |
    |     
 ___|___ 
    """,

    """
    |-------
    |      |
    |      _
    |     |_|
    |    --|
    |      |
    |     
 ___|___ 
    """,

    """
    |-------
    |      |
    |      _
    |     |_|
    |    --|--
    |      |
    |     
 ___|___ 
    """,

    """
    |-------
    |      |
    |      _
    |     |_|
    |    --|--
    |      |
    |     / 
 ___|___ 
    """,

    """
    |-------
    |      |
    |      _
    |     |_|
    |    --|--
    |      |
    |     / \
 ___|___ 
    """]
    return gallows

def draw_gallow(wrong_guesses):
    '''
        Print the gallow using the number of wrong guesses
    '''
    
    n_errors = len(wrong_guesses)
    
    gallows = gallows_list()
    print(gallows[n_errors]) 

def print_header(wrong_guesses,correct_guesses):
    '''
        Print the header of each round
    '''
    
    draw_gallow(wrong_guesses)
    print()
    print('Letras erradas já escolhidas: ', ' '.join(wrong_guesses))
    print()
    print('Palavra: ', ' '.join(correct_guesses))
    print()
    print()

def guess_letter(wrong_guesses,correct_guesses):
    '''
        Get a guess from the user to found out the word
    '''
    
    letter = input('Escolha uma letra: ').lower()
    while (len(letter) != 1) or (not(letter.isalpha())) or (letter in wrong_guesses+correct_guesses):
        if len(letter) > 1:
            reason = 'não pode haver mais de uma letra escolhida'
        elif len(letter) == 0:
            reason = 'deve ser escolhida uma letra'
        elif not(letter.isalpha()):
            reason = 'deve ser uma letra e não um dígito'
        elif letter in wrong_guesses+correct_guesses:
            reason = 'a letra já foi escolhida anteriormente'
            
        letter = input(f'Entrada inválida, pois {reason}.\nPor favor, escolha uma letra válida: ').lower()
    return letter
    
def try_guess(word,letter,wrong_guesses,correct_guesses):
    '''
        Test the guessed letter against the word
    '''    
    
    from copy import deepcopy
    correct_guesses = deepcopy(correct_guesses)
    wrong_guesses = deepcopy(wrong_guesses)
    
    letter_is_found = False
    for i, n in enumerate(word):
        if n == letter:
            correct_guesses[i] = letter
            letter_is_found = True       
    
    if not(letter_is_found):
        wrong_guesses.append(letter)
    
    return wrong_guesses,correct_guesses

def initialize_lists(word):
    '''
        Initialize the lists of correct and wrong letters.
        The initial correct_guesses list is a list containing "_" characters
        and its lenght is equal the word's lenght.
        The initial wrong_guesses list is an empty list.
    '''
    
    correct_guesses = list('_'*len(word))
    wrong_guesses = []
    return wrong_guesses,correct_guesses

def clear_screen():
    '''
        Clear the current outputs of the screen
    '''   
    import os

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def main():
    print('Bem-vindo(a) ao Jogo da Forca.')
    
    word = choose_word()
    wrong_guesses,correct_guesses = initialize_lists(word)
    
    n_errors = len(wrong_guesses)
    MAX_N_ERRORS = len(gallows_list())-1 #the maximum number of errors
    
    current_round = 1
    while (n_errors < MAX_N_ERRORS) and ('_' in correct_guesses):
        
        print(f'Tentativa {current_round}.')
        
        print_header(wrong_guesses,correct_guesses)                

        letter = guess_letter(wrong_guesses,correct_guesses)
        
        wrong_guesses, correct_guesses = try_guess(word,letter,wrong_guesses,correct_guesses)
        
        n_errors = len(wrong_guesses)
        
        clear_screen()
        
        current_round += 1
        
    else:
    
        print_header(wrong_guesses,correct_guesses)
        
        if (n_errors >= MAX_N_ERRORS):
            print(f'Game Over! :( \nA palavra era {word}.')
        else:
            print(f'Parabéns, você acertou após {current_round-1} tentativas! :)')

main()
