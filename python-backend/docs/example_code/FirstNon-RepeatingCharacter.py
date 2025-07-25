from collections import Counter

def first_non_repeating(s):
    freq = Counter(s)
    for c in s:
        if freq[c] == 1:
            return c
    return None

# Example
print(first_non_repeating("abbcdeff"))  
