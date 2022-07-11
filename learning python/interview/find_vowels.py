def find_vowels(sentance, vowels):
    count = 0
    for word in sentance:
        if word.lower() in vowels:
            count += 1
    print(count)



vowels = ['a', 'e', 'i', 'o', 'u']
sentance = "Why?"
find_vowels(sentance, vowels)