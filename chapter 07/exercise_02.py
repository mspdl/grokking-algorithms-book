nodes = ('A', 'B', 'C', 'D', 'E')

distances = {
    'A': {'B': 10},
    'B': {'D': 20},
    'C': {'B': 1},
    'D': {'C': 1, 'E': 30},
    'E': {},
}

start, end = nodes[0], nodes[-1]

def find_route(current, end):
    unvisited = {node: float('inf') for node in nodes}
    current_distance = 0
    unvisited[current] = current_distance
    visited, parents = {}, {}
    while unvisited:
        min_vertex = min(unvisited, key=unvisited.get)
        for neighbour, distance in distances[current].items():
            if distance < 0:
                return None, None
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

if parents == None or distance == None:
    print("It's not possible to find the nearest path with a negative vertice!")
else:  
  path = end
  for toX, fromX in list(reversed(parents.items())):
    if end == toX:
        path += " >- " + fromX
        end = fromX
      
  print("travelled path = " + path[::-1])
  print("travelled distance = " + str(distance))