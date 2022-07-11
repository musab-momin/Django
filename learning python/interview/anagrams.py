#first get the frequency of both the word
#consider both strings as anagram by creating a variable wiht True value 
#then travel any one frequency object and check is the value for the current character is same in the 
#other frequency object or not. if you find any one character which not satisfying the condition 
# break the loop and mark flag as False and print not anagram 


def frequency(word):
    tmp = {}
    for char in word:
        if char != " ":
            if char in tmp.keys():
                tmp[char] = tmp[char] + 1
            else:
                tmp[char] = 1
    return tmp

def is_anagram(first, second):
    if len(first) == len(second):
        first_frequency = frequency(first.lower())
        second_frequency = frequency(second.lower())
        flag = True
        for key in first_frequency.keys():
            if first_frequency[key] != second_frequency[key]:
                flag = False
                break
        print("Anagram" if flag else "not anagram" )
    else:
        print('not a anagram')


#is_anagram(first, second)