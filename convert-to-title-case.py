# cook your dish here

def solve():
    nums = int(input())
    strings = []
    for i in range(nums):
        string = input()
        strings.append(string)
    
    for sentence in strings:
        sentence_list = sentence.split(" ")
        for i in range(len(sentence_list)):
            if sentence_list[i] == "":
                pass
            elif sentence_list[i].upper() == sentence_list[i]:
                pass
            else:
                sentence_list[i] = sentence_list[i].title()
                
        print(" ".join(sentence_list))


if __name__ == "__main__":
    solve()