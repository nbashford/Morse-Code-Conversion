
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def string_to_morse(string_input: str):
    """
    Morse code requires:
        1 space between letters
        3 spaces between words
    function:
        takes the input, converts to uppercase, splits on whitespace
        creates nested list of morse code symbols to respective letter/digit
        join morse code letters in word by 1 space
        join morese code words by 3 spaces
    """

    # Create list of words
    string_words = string_input.upper().split(' ')
    # Nested list of morse code symbols for each letter in each word
    morse_code_words = [[morse_code[letter] for letter in word] for word in string_words]
    # Join letter/digit symbols in word by 1 space, and words by 3 spaces
    morse_code_string = '   '.join([' '.join(word) for word in morse_code_words])

    return morse_code_string


def morse_to_string(morse_input: str):

    """
    Split morse code at every 3 spaces (new word)

    Append the Corresponding letter (Key) if the morse code symbol
    is the value for the morse code key

    Convert string to Lowercase and then Capitalise the first Letter
    """

    # Split at new word indication
    morse_words = morse_input.split('   ')

    string_words = []
    # for each morse code word in morse code string
    for single_word in morse_words:
        words = []
        # for each morse code symbol in morse code word
        for symbol in single_word.split(' '):
            # check if symbol is the corresponding letter keys value
            for letter in morse_code:
                if morse_code[letter] == symbol:
                    # add letter to inner list
                    words.append(letter)
        # add word list to outer list
        string_words.append(words)

    # Join letters of each word, then join words and capitalise first word
    string_words = ' '.join([''.join(word) for word in string_words]).capitalize()

    return string_words


print("Welcome to the Morse Code conversion application.\n")

play = True
while play:
    # Instructions
    response = input("Please enter either a word/sentence(s), or"
                     " morse code: \n")

    # if input is valid morse code
    if set(response) <= {'.', '-', ' '}:
        # print the readable string
        print(f"Your Morse Code Translates to:\n"
              f"{morse_to_string(response)}")
    # if input is not morse code
    else:
        try: # convert input into morse code
            print(f"Your input in morse code is:\n"
                  f"{string_to_morse(response)}")
        except KeyError: # an input not within morse code dictionary keys
            print("Your input is either outside the range of expected characters" 
                  " for morse code, or your morse code includes an incorrect character"
                  " \n please try again")

    continue_play = input("Continue (Y or N) ?\n").lower()
    if continue_play == 'y':
        continue
    elif continue_play == 'n':
        play = False
