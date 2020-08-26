import time
from random_word import RandomWords

r = RandomWords()

# makes array of words and chooses them

words = []

wordNum = int(input("How many words per sentence: "))

for x in range(0,wordNum):
    words.append(r.get_random_word())


def sentence():
    sentence = words[0]
    for x in range(1,len(words)):
        sentence = sentence + " " + words[x]