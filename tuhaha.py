# Unique words and letter frequency from corpus.

import os
import re


# Opens every file in a directory and removes non-text.
def read_n_nuke(path,flag=False):
    dir = path + '/'
    lines = []
    for files in os.listdir(path):
        if os.path.isfile(os.path.join(path, files)):
            with open(dir + files, encoding="utf-8") as f:
                newlines = f.readlines()
                for i in newlines:
                    # Nukes \n, and nonalphas. Need to kill \u2028 types. Oh well.
                    lines.append(str(i).rstrip('\n').lower().replace(r"[^a-z]", " "))
    print("len " + str(len(lines)))
    oneline = ''.join(lines)
    if flag:
        oneline = re.sub(r"[^aeiouhkmnprtwg ]", "", oneline)
    else:
        oneline = re.sub(r"[^a-z ]","",oneline)
    clump = oneline.replace(' ', '')
    split = oneline.split()
    dictionary = []
    trunc_dictionary = []
    for word in split:
        if word not in dictionary:
            dictionary.append(word)
            if len(word) > 2:
                trunc_dictionary.append(word)

    trunc_dictionary = sorted(trunc_dictionary, key=lambda el: len(el))
    dictionary = sorted(dictionary, key=lambda el: len(el))

    uniqueoneline = list(set(clump))
    print(uniqueoneline)

    #alphabetlist = ['a', 'e', 'i', 'o', 'u', 'h', 'k', 'm', 'n', 'o', 'p', 'r', 't', 'w', 'g']
    alphabetlist = uniqueoneline
    freqdictionary = {}
    for letter in alphabetlist:
        freqdictionary.update({letter: clump.count(letter)})

    rawfreqdictionary = freqdictionary
    print(rawfreqdictionary)

    ##freqdictionary.update({'ng': freqdictionary.get("g")})
    ##freqdictionary.update({'n': (freqdictionary.get('n') - freqdictionary.get('g'))})
    ##freqdictionary.pop('g')

    #print(freqdictionary)
    print(trunc_dictionary)
    print(dictionary)
    return uniqueoneline


alphabet1 = read_n_nuke("putunga korero",True)
alphabet2 = read_n_nuke("tarehu")
print()
print()

print(alphabet1)
print(alphabet2)


