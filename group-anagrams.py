def group_anagrams(anagrams_list):
    grouped_anagrams = {}
    for element in anagrams_list:
        key = "".join(sorted(element))
        if key in grouped_anagrams:
            grouped_anagrams[key].append(element)
        else:
            grouped_anagrams[key] = [element]
    return list(grouped_anagrams.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


"""
Time: O(n * m log m)
Space: O(n)
"""
