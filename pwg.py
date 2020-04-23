#!/usr/bin/python3

import itertools

def generate(vals="letters"):
    return list(("".join(x) for x in itertools.chain.from_iterable(itertools.permutations(vals,i+1) for i in range(0,len(vals)))))

# Generate all possible words using letters: a b c:
words = generate("abc")

# Print out the words
for word in words:
    print(word)
