# Unique words and letter frequency from corpus.

import os
import re

# Opens every file in the corpus directory and removes non-text.
path = r"putunga korero"
dir = "putunga korero/"
lines = []
for files in os.listdir(path):
    if os.path.isfile(os.path.join(path, files)):
        with open(dir+files,encoding="utf-8") as f:
            newlines = f.readlines()
            for i in newlines:
                # Nukes \n, and nonalphas. Need to kill \u2028 types. Oh well.
                lines.append(i.rstrip('\n').lower().replace(r"[^a-z]", " "))
            #print(lines)

print(len(lines))
oneline = ''.join(lines)
oneline = re.sub(r"[^aeiouhkmnoprtwg ]", "", oneline)
clump = oneline.replace(' ','')
split = oneline.split()
dictionary = []
for word in split:
    if word not in dictionary and len(word) > 2:
        dictionary.append(word)
dictionary = sorted(dictionary, key=lambda el: len(el))

alphabetlist = ['a','e','i','o','u','h','k','m','n','o','p','r','t','w','g']

for letter in alphabetlist:
    print(clump.count(letter))
