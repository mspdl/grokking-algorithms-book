def biggest(list):
  if len(list) < 2:
    return 'Invalid list size'
  if len(list) == 2:
    return list[0] if list[0] > list[1] else list[1]
  second_biggest_number = biggest(list[1:])
  return list[0] if list[0] > second_biggest_number else second_biggest_number

print("Biggest number on the list [5,1,3,4] =  " + str(biggest([5,1,3,4])))
print("Biggest number on the list [1] =  " + str(biggest([1])))