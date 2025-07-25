from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

# Example
print(group_anagrams(['bat', 'tab', 'tap', 'pat']))
# Output: [['bat', 'tab'], ['tap', 'pat']]
