def pyramid(num):
    mid = (num * 2 -1) // 2
    for row in range(num):
        level = ''
        for col in range((num+num) - 1):
            if mid - row <= col and mid + row >= col:
                level += '#'
            else:
                level += ' '
        print(level)

pyramid(10)