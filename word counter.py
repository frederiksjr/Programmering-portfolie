from string import *
from collections import defaultdict
from operator import itemgetter
import re

number = 10
words = {}
total_words = 0
words_only = re.compile(r'^[a-z]{2,}$')
counter = defaultdict(int)

"""Define function to count the total number of words"""
def count_words(s):
    unique_words = split(s)
    return len(unique_words)

"""Define words as 2 letters or more -- no single letter words such as "a" """
for word in words:
    if len(word) >= 2:
        counter[word] += 1


"""Open text document, strip it, then filter it"""
txt_file = open('charactermask.txt', 'r')

for line in txt_file:
    total_words = total_words + count_words(line)
    for word in line.strip().split():
        word = word.strip(punctuation).lower()
        if words_only.match(word):
            counter[word] += 1


# Most Frequent Words
top_words = sorted(counter.iteritems(),
                    key=lambda (word, count): (-count, word))[:number] 

print("Most Frequent Words: ")

for word, frequency in top_words:
    print("%s: %d" % (word, frequency))


# Least Frequent Words:
least_words = sorted(counter.iteritems(),
                    key=lambda (word, count): (count, word))[:number]

print("")
print("Least Frequent Words: ")

for word, frequency in least_words:
    print("%s: %d" % (word, frequency))


# Total Unique Words:
print(" ")
print("Total Number of Words: %s" % total_words)