def has_loop(node_map, current=1, visited=None):
    if visited is None:
        visited = set()
    if current is None:
        return False
    if current in visited:
        return True
    visited.add(current)
    return has_loop(node_map, node_map.get(current), visited)
'''

def has_loop(node_map):
    visited = set()
    current = next(iter(node_map))  # Starting from the first node
    while current is not None:
        if current in visited:
            return True
        visited.add(current)
        current = node_map.get(current)
    return False
'''
# Example
print(has_loop({1: 2, 2: 3, 3: 4, 4: 5},1))  # Output: True
