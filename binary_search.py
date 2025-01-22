array = (1,2,3,4,5,6,8)

def binary_search(array, target):
    left = 0
    right = len(array)

    while left < right:
        mid = int((left+right) / 2)
        actual = array[mid]

        if actual == target:
            return mid
        elif actual < target:
            left = mid + 1
        else:
            right = mid
    return -1


print("Index is: ", binary_search(array, 1))
print("Index is: ", binary_search(array, 4))
print("Index is: ", binary_search(array, 5))
print("Index is: ", binary_search(array, 7))
print("Index is: ", binary_search(array, 8))
