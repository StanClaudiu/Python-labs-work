def findLoop(mapper) :
    visited = []
    current = "start"
    while current not in visited :
        visited.append(current)
        current = mapper.get(current)
    return visited

print(findLoop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))