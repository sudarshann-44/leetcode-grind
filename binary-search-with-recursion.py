

def binary_search(arr, search_ele, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if arr[mid] == search_ele:
            return mid
        elif arr[mid] > search_ele:
            low = mid + 1
        else:
            high = mid - 1
        binary_search(arr, search_ele, low, high)


print(binary_search([1, 3, 5, 7, 9], 5, 0, 4))