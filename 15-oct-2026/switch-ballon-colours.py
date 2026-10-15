
# Problem : https://www.codechef.com/practice/course/strings-new/STRINGSP01/problems/CHN09

def solve():
    testcases_count = int(input())
    strings = []
    for i in range(testcases_count):
        strings.append(input())
    
    for string in strings:
        a_count = 0;
        b_count = 0
        for char in string:
            if char == "a":
                a_count +=1
            else:
                b_count += 1
        if a_count == b_count:
            print(a_count)
        elif a_count > b_count:
            print(b_count)

        else:
            print(a_count)
        
if __name__ == "__main__":
    
    solve()