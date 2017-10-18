#Author: Russell Santos
#Title: Scrambler

from firebase import firebase
firebase = firebase.FirebaseApplication('https://scrambler-76559.firebaseio.com/', None)
make_key_choice = input('Use existing key? (Y/N) ')
if make_key_choice == 'N':
    key_choice = input('Enter a new key: ')
    result = firebase.post(key_choice)
    print (result)
else:
    key_choice = input('Enter key: ')
    result = firebase.get(key_choice, None)
    key_name_gen = (key for key in result)
    key_name = next(key_name_gen)
    r = result.get(key_name)
    print(r)
    

