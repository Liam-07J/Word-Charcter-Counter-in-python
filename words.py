with open('text.txt') as f:
    lines = f.readlines()
text = ''.join(lines)
words = text.split()

words = [word.lower() for word in words]

# convert words to a dictionary and count the number of times each word appears
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)

#write this to a txt file 
with open('word_counts.txt', 'w') as f:
    for word in word_counts:
        f.write(word + ' ' + str(word_counts[word]) + '\n')
        