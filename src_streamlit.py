import random
import streamlit as st
import time
from copy import deepcopy
from PIL import Image
import base64

def choose_word():
    '''
        It randomly chooses a word from the fruit list.
    '''
    
    with open('frutas.txt', 'r') as file: #abre o arquivo já existente
        fruits = file.read().split('\n') #lê o conteúdo do arquivo e o salva na variável        
        
    while '' in fruits:
        fruits.remove('')

    n = random.randrange(len(fruits))

    return fruits[n]

def gallows_list():
    '''
        It returns a list with the file names of the gallows images.
    '''
        
    gallows = ["gallows_0.png","gallows_1.png","gallows_2.png",
               "gallows_3.png","gallows_4.png","gallows_5.png",
               "gallows_6.png","gallows_7_loser.png","gallows_8_winner.png"]
    return gallows

def draw_gallows(wrong_guesses):
    '''
        It prints the gallows using the number of wrong guesses.
    '''  

    n_errors = len(wrong_guesses)   

    gallows = gallows_list()
    image = Image.open(f'project_images/'+gallows[n_errors])
    width, height = image.size
    width //= 4
    height //= 4
    image = image.resize((width,height))
    st.image(image) 

def print_gif(name_file):
    '''
        It prints a gif file on the screen.
    ''' 
    file_ = open("./project_images/"+name_file, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )

def print_header(wrong_guesses,correct_guesses,current_round):
    '''
        It prints the header of each round.
    '''
    st.header(f'Tentativa {current_round}')
    col_1, col_2 = st.columns([1,1])
    
    with col_1:
        st.write('Palavra: ', ' '.join(correct_guesses))
        st.write('Letras erradas já escolhidas: ', ' '.join(wrong_guesses))
    with col_2:
        draw_gallows(wrong_guesses)
    
    st.write('')

def is_letter_valid(letter,wrong_guesses,correct_guesses):
    '''
        It checks if the letter is a valid input and returns
        False if it's not ok and a reason to show to the user why 
        his input is invalid. Finally, it returns True otherwise.
    '''
    
    if len(letter) > 1:
        reason = 'não pode haver mais de uma letra escolhida'
        return False,reason
    elif len(letter) == 0:
        reason = 'deve ser escolhida uma letra'
        return False,reason
    elif not(letter.isalpha()):
        reason = 'deve ser uma letra e não um dígito'
        return False,reason
    elif letter in wrong_guesses+correct_guesses:
        reason = 'a letra já foi escolhida anteriormente'
        return False,reason
    else:
        return True,''

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

def update_text_input():
    '''
        Function to be used in the callback of the streamlit button.
        It keeps the input letter in "letter" key of the streamlit session_state
        and sets the input box to be "".
    '''
    st.session_state['letter'] = st.session_state[1].lower()
    st.session_state[1] = ''

def print_game_over(word):
    '''
        It prints game over results on the screen 
    '''
    col_1, col_2 = st.columns([1,1])
    with col_1:
        st.write(f'Game Over!')
        st.write(f'A palavra era {word}.')
    with col_2:
        print_gif('sad.gif')

def print_congratulations(current_round):
    '''
        It prints congratulations results on the screen 
    '''
    col_1, col_2 = st.columns([1,1])
    with col_1:
        st.write(f'Parabéns!')
        st.write(f'Você acertou após {current_round-1} tentativas.')
    with col_2:
        print_gif('happy.gif')
    

if 'initialized' not in st.session_state:
	st.session_state.initialized = 0

if 'flag_rerun_on_max_error_reached' not in st.session_state:
	st.session_state.flag_rerun_on_max_error_reached = False

if 'flag_rerun_on_word_found' not in st.session_state:
	st.session_state.flag_rerun_on_word_found = False

MAX_N_ERRORS = len(gallows_list())-3  #the maximum number of errors

if st.session_state.initialized == 0:
    word = choose_word()
    st.session_state['word'] = word
    st.session_state['wrong_guesses'] = []
    st.session_state['correct_guesses'] = list('_'*len(word))
    st.session_state['current_round'] = 1
    st.session_state.initialized = 1

    st.title(f"Bem-vindo(a) ao Jogo da Forca.")

if (len(st.session_state['wrong_guesses']) < MAX_N_ERRORS) and ('_' in st.session_state['correct_guesses']):
    
    with st.form(key='0'):
        st.text_input('Escolha uma letra: ',key=1)
        if st.form_submit_button('Ok',on_click = update_text_input):  
            letter = st.session_state['letter']
            is_valid,reason = is_letter_valid(letter,st.session_state['wrong_guesses'],st.session_state['correct_guesses'])
            if is_valid:        
                st.session_state['wrong_guesses'],st.session_state['correct_guesses']\
                = try_guess(st.session_state['word'],letter,\
                st.session_state['wrong_guesses'],st.session_state['correct_guesses'])
                
                st.session_state['current_round'] += 1
            else:
                st.write(f'Entrada inválida, pois {reason}.')

if (len(st.session_state['wrong_guesses']) < MAX_N_ERRORS) and ('_' in st.session_state['correct_guesses']):
    print_header(st.session_state['wrong_guesses'],st.session_state['correct_guesses'],st.session_state['current_round'])
else:
    if (len(st.session_state['wrong_guesses']) >= MAX_N_ERRORS):
        if not(st.session_state.flag_rerun_on_max_error_reached):
            print_header(st.session_state['wrong_guesses'],\
                         st.session_state['correct_guesses'],\
                         st.session_state['current_round']-1)
            
            st.session_state.flag_rerun_on_max_error_reached = True
            
            st.experimental_rerun()
        else:
            time.sleep(1)
            print_header(st.session_state['wrong_guesses']+[''],\
                         st.session_state['correct_guesses'],\
                         st.session_state['current_round']-1)

            word = st.session_state['word']
            
            print_game_over(word)
            
            st.session_state.flag_rerun_on_max_error_reached = True
        
    elif not('_' in st.session_state['correct_guesses']):
        if not(st.session_state.flag_rerun_on_word_found):
            print_header(st.session_state['wrong_guesses'],\
                         st.session_state['correct_guesses'],\
                         st.session_state['current_round']-1)
            st.session_state.flag_rerun_on_word_found = True 
            st.experimental_rerun()
        else:
            complement = ['' for _ in range(8-len(st.session_state['wrong_guesses']))]
            print_header(st.session_state['wrong_guesses']+complement,\
                         st.session_state['correct_guesses'],\
                         st.session_state['current_round']-1)
            current_round = st.session_state['current_round']
            print_congratulations(current_round)
            st.session_state.flag_rerun_on_word_found = True    