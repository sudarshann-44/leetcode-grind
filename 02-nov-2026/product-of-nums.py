class Solution(object):
    def multiply(self, num1, num2):
        hashmap = { str(i): i for i in range(0, 10)}
        ans = ""
        carry = 0
        i = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        while i < len(num1):
            product = hashmap[num1[i]] * hashmap[num2[i]] + carry
            ans = str(product) + ans
            i+=1
        return ans
 
sol = Solution()
print(sol.multiply("123", "456"))