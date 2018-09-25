
def alphabet_position(letter):

    #global all_sym
    all_sym = {'alphabet' : "abcdefghijklmnopqrstuvwxyz" , 'ALPHABET' : "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'sym' : "'!@#$%^&*()_+=-?/.,><:; ", 'num' : '1234567890'}  
    if letter in all_sym['sym']:
        letter_pos = letter
    elif letter in all_sym['num']:
        letter_pos = letter
    elif letter == letter.lower():
        if letter in all_sym['alphabet']:
            letter_pos = all_sym['alphabet'].index(letter)
    elif letter == letter.upper():
        if letter in all_sym['ALPHABET']:
            letter_pos = all_sym['ALPHABET'].index(letter)
    return letter_pos

def rotate_character(char,rot):
    #global all_sym
    all_sym = {'alphabet' : "abcdefghijklmnopqrstuvwxyz" , 'ALPHABET' : "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'sym' : "'!@#$%^&*()_+=-?/.,><:; ",'num' : '1234567890'} 
    if char in all_sym['sym']:
        encrypt = char
    elif char in all_sym['num']:
        encrypt = char    
    elif char == char.lower():
        rota = all_sym['alphabet'].index(char) + int(rot)
        if rota < 26:
            encrypt = all_sym['alphabet'][rota]
        else:
            encrypt = all_sym['alphabet'][rota % 26] 
    elif char == char.upper():
        ROTA = all_sym['ALPHABET'].index(char) + int(rot)
        if ROTA < 26:
            encrypt = all_sym['ALPHABET'][ROTA]
        else:
            encrypt = all_sym['ALPHABET'][ROTA % 26]
    return encrypt
        