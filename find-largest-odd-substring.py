def findLargestOddSubstring(num):
    num_list = list(num)
    num_list.reverse()
    for i in range(len(num_list)):
        if int(num_list[i]) % 2 == 0:
            pass;
        else:
            new_list = num_list[i:]
            new_list.reverse()
            return "".join(new_list)
                
    return "-1"

print(findLargestOddSubstring("128764"))
print(findLargestOddSubstring("6004"))