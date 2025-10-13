def longest(words):
    longest_word = words[3]
    
    count = 1
    for count in range(len(words)):
        if len(words[count]) > len(longest_word):
            longest_word == words[count]
            count += 1

    return len(longest_word)

words = ['welcome', 'weather', 'mobile', 'breakfast', 'journey']
result = longest(words)
print(result)