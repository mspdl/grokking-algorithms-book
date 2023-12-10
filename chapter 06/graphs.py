from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search_queue():
  search_queue = deque()
  search_queue += graph["you"]

  while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
      print(str(person) + " is a mango seller!")
      return True
    else:
      print(str(person) + " is NOT a mango seller!")
      search_queue += graph[person]
  return False

def person_is_seller(name):
  return name[-1] == 'm'

print("=== Search Queue Result ===")
search_queue()
print("======")

def search(name):
  search_queue = deque()
  search_queue += graph[name]
  checkedNames = []
  while search_queue:
    personName = search_queue.popleft()
    if not personName in checkedNames:
      if person_is_seller(personName):
        print(str(personName) + " is a mango seller!")
        return True
      else:
        search_queue += graph[personName]
        checkedNames.append(personName)
  return False

print("=== Search Result ===")
search("you")
print("======")