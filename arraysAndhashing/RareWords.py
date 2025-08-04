import re
from collections import defaultdict

def rare_words_finder(text):
    words = re.findall(r'\w+', text.lower())
    freq = defaultdict(int)
    first_seen = {}

    for i, word in enumerate(words):
        freq[word] += 1
        if word not in first_seen:
            first_seen[word] = i

    # Ordenamos por frecuencia ascendente, luego por orden de aparición
    sorted_words = sorted(freq.items(), key=lambda x: (x[1], first_seen[x[0]]))

    return sorted_words[:5]

print(rare_words_finder("Hey there hot shot Are you ready for a challenge This might be trickier than it looks")) # Expected Output: [('hey', 1), ('there', 1), ('hot', 1), ('shot', 1), ('are', 1)]

print(rare_words_finder("The quick brown fox jumps over the lazy dog The fox is quick but the dog is lazy")) # Expected Output: [('brown', 1), ('jumps', 1), ('over', 1), ('but', 1), ('quick', 2)]

print(rare_words_finder("")) # Expected Output: []