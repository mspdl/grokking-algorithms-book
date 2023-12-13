nodes = ('A', 'B', 'C', 'D', 'E', 'F')

distances = {
    'A': {'C': 5, 'B': 2},
    'B': {'C': 8, 'E': 7},
    'C': {'D': 4, 'E': 2},
    'D': {'F': 3},
    'E': {'F': 1},
    'F': {}
}

start, end = 'A', 'F'

def find_route(current, end):
    unvisited = {node: float('inf') for node in nodes}
    current_distance = 0
    unvisited[current] = current_distance
    visited, parents = {}, {}
    while unvisited:
        min_vertex = min(unvisited, key=unvisited.get)
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: 
                continue
            new_distance = current_distance + distance
            if unvisited[neighbour] is float('inf') or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
                parents[neighbour] = min_vertex
        visited[current] = current_distance
        unvisited.pop(min_vertex)
        if min_vertex == end: 
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = min(candidates, key=lambda x: x[1])
    return parents, new_distance

parents, distance = find_route(start, end)

path = end
for toX, fromX in list(reversed(parents.items())):
   if end == toX:
      path += " >- " + fromX
      end = fromX
    
print("travelled path = " + path[::-1])
print("travelled distance = " + str(distance))