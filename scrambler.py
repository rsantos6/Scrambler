#Author: Russell Santos
#Title: Scrambler


def main():
    
    make_key_choice = input('Use existing key? (Y/N): ')
    while make_key_choice not in ['Y', 'N']:
        print(make_key_choice + ' is an invalid command')
        make_key_choice = input('Use existing key? (Y/N): ')
            
    if make_key_choice == 'N':
        scrambled = make_new_key()
    elif make_key_choice == 'Y':
        scrambled = get_old_key()

    write_message_bool = input('Write or read message? (write/read): ')
    while write_message_bool not in ['write', 'read']:
        print(write_message_bool + ' is an invalid command')
        write_message_bool = input('Write or read message? (write/read): ')

    if write_message_bool == 'write':
        write_message(scrambled)
    elif write_message_bool == 'read':
        read_message(scrambled)

def loop(scrambled):
    go_again = input('Go again? (Y/N): ')
    while go_again not in ['Y', 'N']:
        print(go_again + ' is an invalid command')
        go_again = input('Use existing key? (Y/N): ')
    if go_again == 'Y':
        use_same_key = input('Use same key? (Y/N): ')
        while use_same_key not in ['Y', 'N']:
            print(use_same_key + ' is an invalid command')
            use_same_key = input('Use same key? (Y/N): ')
        if use_same_key == 'Y':
            read_write = input('Write or read message? (write/read): ')
            while read_write not in ['write', 'read']:
                print(read_write + ' is an invalid command')
                read_write = input('Write or read message? (write/read): ')
            if read_write == 'write':
                write_message(scrambled)
            elif read_write == 'read':
                read_message(scrambled)
        elif use_same_key == 'N':   
            main()
    
def get_old_key():
    key_choice = input('Enter key: ')
    result = firebase.get(key_choice, None)
    while result is None:
        print(key_choice + ' is not an existing key')
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
    loop(scrambled)

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
    loop(scrambled)

if __name__ == '__main__':
    import random
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://scrambler-76559.firebaseio.com/', None)
    main()

