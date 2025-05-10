# #lcsw_136_SingleNumber
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tdict={}
        for i in nums:
            if i in tdict:
                tdict[i]+=1
            else:
                tdict[i]=1
        for k, v in tdict.items():
            if v == 1:
                return k
            


solution = Solution()
print(solution.singleNumber([2, 2, 1]))  # Should return 1
print(solution.singleNumber([4, 1, 2, 1, 2]))  # Should return 4
print(solution.singleNumber([1]))  # Should return 1

    

