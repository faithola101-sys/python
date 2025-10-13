def get_string(word):

for i in range(len(word)):

    if len(word) < 2:
    return 0
    first = word[0]
    second = word[1]
    eight = word[7]    
    ninth = word[8]
    return first, second, eighth, ninth


word = "semicolon"
result = get_string(word)
print(result)