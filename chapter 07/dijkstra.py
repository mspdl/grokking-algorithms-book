graph = {}

graph["start"] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['end'] = 3

graph['b'] = {}
graph['b']['a'] = 5
graph['b']['end'] = 5

graph['end'] = {}

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = float("inf")

parents = {}
parents['a'] = "start"
parents['b'] = "start"
parents['end'] = None

processed = []

def find_the_lighter(costs):
  lighter = float("inf")
  lighter_node = None
  for node in costs:
    cost = costs[node]
    if cost < lighter and node not in processed:
      lighter = cost
      lighter_node = node
  return lighter_node

node = find_the_lighter(costs)

while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  for n in neighbors.keys():
    new_cost = cost + neighbors[n]
    if costs[n] > new_cost:
      costs[n] = new_cost
      parents[n] = node
  processed.append(node)
  node = find_the_lighter(costs)
  
print("shortest path = " + str(parents))
print("shortest path weight = " + str(cost))

