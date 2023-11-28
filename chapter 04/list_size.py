def list_size(list):
  if list == []:
    return 0
  return 1 + list_size(list[1:])

print("Size of the list [1,3,4] =  " + str(list_size([1,3,4])))