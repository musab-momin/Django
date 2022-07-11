#This is a dictory app where user can enter any word and program will retur defination of it
#we are using a json file to show defination of work "To load json file into python we have standard json library which we have to import

import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('json_dict.json'))


def take_input():
    usr_inp = input('>')
    return usr_inp

def find_defination(word):
    word = word.lower()
    #It seems prettry easy program but what if user miss spelled something we have to give suggestion to user
    #for eg instead of rain user typed rainn we need to give user a suggestion like google does by askin did you mean rain something like this
    #to do this we don't need to code it from scrach we have a standard library Difflib and it has one method called SequenceMatcher we will use it
    #this method will take two arguments first is function if we have any spaces in our string or something like that but in our case we don't have that issue so we pass None
    #after passing none we have to pass two string whom which we are trying to find similarity after calling function call .ratio() method on it so it will give float number
    if word in data:
        return data[word]
    elif word[0].upper() in data:
        return data[word[0].upper()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        #SequenceMatcher(None, 'rainn', 'rain') this is just an example
        suggestions_arr = get_close_matches(word, data.keys()) #this is another difflib method which gives array of close matches to string by default it will give 3 words but we are intrested in first one that's why [0]
        if len(suggestions_arr) > 0:
            confirmation = input(f'Did you mean {suggestions_arr[0]} press y for yes and n for no\n').lower()
            if confirmation == 'y':
               return data[suggestions_arr[0]]
            elif confirmation == 'n':
                return "We didn't understand your input. please try again!"
            else:
               return 'Defination not found' 
        else:
            return 'Defination not found'

word = take_input()
definations = find_defination(word)
if type(definations) == list:
    for defination in definations:
        print(defination)
else:
    print(definations)

