#lcsw_349_Intersection_of_TwoArrays
from typing import List 
class Solution:
    def intersection(self, nums1: List[int]=[], nums2: List[int]=[]) -> List[int]:

        tdict={}
        tdict2={}
        anslist=[]
        for i in nums1 :
            if i in tdict:
                tdict[i]+=1
            else:
                tdict[i]=1

        for i in nums2 :
            if i in tdict2:
                tdict2[i]+=1
            else:
                tdict2[i]=1
            
        for k in tdict:
            if k in tdict2 :
                anslist.append(k)
        return anslist

solution = Solution()
print(solution.intersection([1, 2, 2, 1], [2, 2]))  # [2]
print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4]
print(solution.intersection([1, 2, 3], [4, 5, 6]))  # []
print(solution.intersection([1,3,4],[2,1,2]))  # [1]
