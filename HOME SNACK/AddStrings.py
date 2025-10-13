
def add_ing(word):

  for i in range(len(word)):
    word[0] = "abc" + 'ing'
    return word[0]

word = ["abc","do"]
result = add_ing(word)
print(result)