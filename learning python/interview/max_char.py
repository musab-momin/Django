#In the given string find the character which is commonaly used

def common(test):
    frequency = {}
    max = 0
    common_char = ''
    for char in test:
        if char in frequency.keys():
            frequency[char] = frequency[char]+1
        else:
            frequency[char] = 1
    for key, value in frequency.items():
        if value > max:
            common_char = key
    print(f"most commonaly used character is '{common_char}'")

test = "Hello There"
common(test)