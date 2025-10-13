def odd_index_letters(word):
    result = ""
    for i in range(len(word)):
        if i % 2 != 0:
            result += word[i]
    return result

word = 'semicolon'   
result = odd_index_letters(word)
print(result)