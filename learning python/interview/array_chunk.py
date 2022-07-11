def create_chunks(arr, size):
    chunks= []
    index = 0

    while index < len(arr):
        chunks.append( arr [index : (index+size) ] )
        index = index + size

    print(chunks)
arr = [1, 2, 3, 4, 5]
size = 3
create_chunks(arr, size)