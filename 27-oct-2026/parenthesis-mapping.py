# https://leetcode.com/problems/generate-parentheses/
# It's a backtracking algo I took help of chatGPT

def match_parenthesis(collection, current = "", open_count = 0, close_count = 0, threshold = -1):
    if open_count == close_count == threshold:
        collection.append(current)
    
    if open_count < threshold:
        match_parenthesis( collection, current + "(", open_count + 1, close_count, threshold, )
    
    if close_count < open_count:
        match_parenthesis(collection, current + ")", open_count, close_count + 1, threshold)

def main(threshold):
    ans = []
    start = ""
    match_parenthesis(ans, start, 0, 0, threshold)
    return ans

print(main(3))