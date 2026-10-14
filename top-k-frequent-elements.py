

def top_k_frequent(nums, k):
    frequency_tracker = {}
    for num in nums:
        # default value of 0 is used if num is not already in the dictionary
        frequency_tracker[num] = frequency_tracker.get(num, 0) + 1

    # enabled reverse sorting with key
    return sorted(frequency_tracker.keys(), key=lambda x: frequency_tracker[x], reverse=True)[:k]


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))