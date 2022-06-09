def findSmallest (arr):
    smallest = arr[0] # store smallest value
    smallest_index = 0 # store smallest value index

    for i in range(1, len(arr)): # loop through all the items in the array
        if arr[i] < smallest: # verifies if the item in that index of the array is less than the current smallest value
            smallest = arr[i] # if smaller, change smallest to that new value
            smallest_index = i # update the index
    return smallest_index # return the index of the smaller value

def selectionSort (arr): # sorts the array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) # finds the smallest element in the array
        newArr.append(arr.pop(smallest)) # adds that value to the new array
    return newArr

print(selectionSort([5,3,6,2,10,1,11,4,7]))