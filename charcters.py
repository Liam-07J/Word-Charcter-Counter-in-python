with open('text.txt') as f:
    lines = f.readlines()
text = ''.join(lines)
#split into chacters
chars = list(text)

chars = [chars.lower() for chars in chars]


# convert chars to a dictionary and count the number of times each chars appears
chars_counts = {}
for chars in chars:
    if chars in chars_counts:
        chars_counts[chars] += 1
    else:
        chars_counts[chars] = 1
print(chars_counts)

#write this to a txt file 
with open('chars_counts.txt', 'w') as f:
    for chars in chars_counts:
        f.write(chars + ' ' + str(chars_counts[chars]) + '\n')    