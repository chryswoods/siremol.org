# Distributed Mapping : Answer to exercise 1

```python
import sys
import re

from scoop import futures

def count_words(filename):
    """Count the number of times every word in the file `filename`
       is contained in this file. Return the result as a dictionary,
       where the key is word, and the value is the number of times
       the word appears in the file"""
    lines = open(filename, "r").readlines()

    all_words = {}

    for line in lines:
        words = line.split(" ")

        for word in words:
            #lowercase the word and remove all
            #characters that are now [a-z] or hyphen
            word = word.lower()
            match = re.search(r"([a-z\-]+)", word)

            if match:
                word = match.groups()[0]
                
                if word in all_words:
                    all_words[word] += 1
                else:
                    all_words[word] = 1

    return all_words

def reduce_dicts( dict1, dict2 ):
    """Combine (reduce) the passed two dictionaries to return
       a dictionary that contains the keys of both, where the
       values are equal to the sum of values for each key"""

    # explicitly copy the dictionary, as otherwise
    # we risk modifying 'dict1'
    combined = {}

    for key in dict1.keys():
        combined[key] = dict1[key]

    for key in dict2.keys():
        if key in combined:
            combined[key] += dict2[key]
        else:
            combined[key] = dict2[key]

    return combined

if __name__ == "__main__":

    filenames = sys.argv[1:]

    words = futures.mapReduce( count_words, reduce_dicts, filenames )

    keys = words.keys()
    keys.sort()

    for key in keys:
        if words[key] > 2000:
            print("%s == %s" % (key, words[key]))
```

***

# [Previous](mapreduce_part3.md) [Up](mapreduce_part3.md) [Next](mapreduce_part3.md)
