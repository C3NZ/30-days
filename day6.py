num_words = int(input())
words = []

for i in range(num_words):
    words.append(input())

output = []
for word in words:
    even_word = ""
    odd_word = ""
    
    for i in range(len(word)):
        if i % 2 == 0:
            even_word += word[i]
        else:
            odd_word += word[i]
            
    output.append(even_word + " " + odd_word)

for word in output:
    print(word)