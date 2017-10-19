#Author: Russell Santos
#Title: Scrambler


def main():
    make_key_choice = input('Use existing key? (Y/N): ')

    if make_key_choice == 'N':
        scrambled = make_new_key()
    elif make_key_choice == 'Y':
        scrambled = get_old_key()

    write_message_bool = input('Write or read message? (write/read): ')

    if write_message_bool == 'write':
        write_message(scrambled)
    elif write_message_bool == 'read':
        read_message(scrambled)
    
def get_old_key():
    key_choice = input('Enter key: ')
    result = firebase.get(key_choice, None)
    key_name_gen = (key for key in result)
    key_name = next(key_name_gen)
    return result.get(key_name)

def make_new_key():
    key_choice = input('Enter a new key: ')
    language_string = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-/.,><;'
    language_array = list(language_string)
    language = []
    for symbol in language_array:
        rand_num = random.randint(0,len(language_string)-1)
        symbol_pair = (symbol, language_string[rand_num])
        language_string = language_string.replace(language_string[rand_num], "")
        language.append(symbol_pair)
    firebase.post(key_choice, language)
    return language

def write_message(scrambled):
    message = input('Enter the message you want to encode: ')
    new_message = ""
    message_array = list(message)
    for letter in message_array:
        if letter == ' ':
            new_message += ' '
        else:
            corresponding_pair = (x for x in scrambled if letter.lower() == x[0])
            corresponding_pair = next(corresponding_pair)
            new_message += corresponding_pair[1]
    print(new_message)

def read_message(scrambled):
    message = input('Enter the message you want to decode: ')
    new_message = ""
    message_array = list(message)
    for letter in message_array:
        if letter == ' ':
            new_message += ' '
        else:
            corresponding_pair = (x for x in scrambled if letter.lower() == x[1])
            corresponding_pair = next(corresponding_pair)
            new_message += corresponding_pair[0]
    print(new_message)

if __name__ == '__main__':
    import random
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://scrambler-76559.firebaseio.com/', None)
    main()

