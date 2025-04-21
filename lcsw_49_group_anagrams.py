#lcsw_49_group_anagrams
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wd={}
        for i in strs :

            tempsortedi=tuple(sorted(i))
            if tempsortedi not in wd :
                wd[tempsortedi]=[i]
            elif tempsortedi in wd :
                wd[tempsortedi].append(i)
            

        return list(wd.values())
solution=Solution()
strs=["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams (strs))
