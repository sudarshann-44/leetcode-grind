# Problem : https://leetcode.com/problems/minimum-index-sum-of-two-lists/


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashmap = { value: index for index, value in enumerate(list1) if value in list2}
        for i in range(len(list2)):
            value = list2[i]
            data = hashmap.get(value, None)
            if data is not None:
                hashmap[value] = hashmap[value] + i
        lowest = min(hashmap.values())
        item = []
        for data in hashmap.items():
            if data[1] < lowest:
                lowest = data[1]
                item = [data[0]]
            elif data[1] == lowest:
                item.append(data[0]) 
        return item
        
        
sol = Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"] 
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(sol.findRestaurant(list1, list2))