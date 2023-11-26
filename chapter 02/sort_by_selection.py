def findSmallestNumberIndex(arr):
    smallest_number = arr[0]
    smallest_number_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_number:
            smallest_number = arr[i]
            smallest_number_index = i
    return smallest_number_index

numbers = [6,5,1,8,0]
smallest_number_index = findSmallestNumberIndex(numbers)
print("numbers = "  + str(numbers))
print("smallest number = " + str(numbers[smallest_number_index]))
print("its index = " + str(smallest_number_index))

def sortBySelection(arr):
    newArray = []
    for i in range(len(arr)):
        smallestNumberIndex = findSmallestNumberIndex(arr)
        newArray.append(arr.pop(smallestNumberIndex))
    return newArray

sortedList = sortBySelection(numbers)
print("sorted numbers = " + str(sortedList))