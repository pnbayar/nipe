def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Example
print(flatten([1, [2, [3, 4], 5]]))  # Output: [1, 2, 3, 4, 5]
