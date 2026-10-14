def binary_search(arr, search_ele):
    start = 0;
    end = len(arr) - 1

    # until start is less than and not equal to end
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == search_ele:
            return f"Found element {search_ele} at index {mid}"
        elif arr[mid] > search_ele:
            # shift end to skip current mid
            end = mid - 1
        else:
            # shift start to skip current mid
            start = mid + 1
    return "Element not found";

print(binary_search([3,9,13,19,25,55,90], 19))
print(binary_search([3,9,13,19,25,55,90], 99))