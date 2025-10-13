
words = ['ada', 'obo', 'aba', 'zy' , 'aza', 'pep',]

count = 0
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1  
        print(f"word == {word}, count == {count}") 
