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

# order the file by the number of times each chars appears
chars_counts_sorted = sorted(chars_counts.items(), key=lambda x: x[1], reverse=True)

#write this to a txt file
with open('chars_counts.txt', 'w') as f:
    for chars in chars_counts_sorted:
        f.write(chars[0] + ' ' + str(chars[1]) + '\n')   