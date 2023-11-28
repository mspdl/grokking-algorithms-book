def sum(list):
  if list == []:
    return 0
  return list[0] + sum(list[1:])

print("Sum of list [1,3,4] =  " + str(sum([1,3,4])))