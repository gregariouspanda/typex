import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

input_text = sys.stdin.read()
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def clean(string):
    clean_list = []
    for char in string:
        if char.upper() in ALPHABET:
            clean_list.append(char.upper())
    return ''.join(clean_list)


letter_appearances = {}

for char in ALPHABET:
    if char not in letter_appearances.keys():
        letter_appearances[char] = 0
for char in clean(input_text):
    if char not in letter_appearances.keys():
        letter_appearances[char] = 1
    else:
        letter_appearances[char] += 1

sorted_keys = list(sorted(letter_appearances.keys()))
value = []
for key in sorted_keys:
    value.append(letter_appearances[key])
y_pos = np.arange(len(value))

plt.bar(y_pos, value, align='center', alpha=1)
plt.xticks(y_pos, sorted_keys)
plt.ylabel('Number of occurances')
plt.xlabel('Letter')
plt.title('Letter Frequency')
plt.show()



