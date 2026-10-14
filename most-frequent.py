# cook your dish here
import sys

def solve():
    input_data = input()
    character_dict = dict()
    for element in input_data:
        element = element.lower()
        if element.isalpha() and element != "" and element != " ":
            if element in character_dict.keys():
                character_dict[element] += 1
            else:
                character_dict[element] = 1

    sorted_dict = dict(sorted(character_dict.items()))
    highest = 0;
    high_key = None
    for key, value in sorted_dict.items():
        if value > highest:
            high_key = key 
            highest = value
    print(high_key)

if __name__ == '__main__':
    solve()