#lcsw_217_ContainsDuplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        tset=set()
        ct=0
        for i in nums :
            if i in tset :
                return True
            tset.add(i)
        return False 
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # Should return True
print(solution.containsDuplicate([1, 2, 3, 4]))  # Should return False
#either sort a list , or use set to reduce time comlplexity for large data sets
#smartest way - comparing set's len


# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         tlist=[]
#         ct=0
#         for i in nums :
#             if i in tlist :
#                 return True
#             tlist.append(i)
#         return False 
# solution = Solution()
