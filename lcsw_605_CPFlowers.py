#lcsw_605_CPFlowers
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans=False
        ct = 0
        flowerbed = [0] + flowerbed + [0]  
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                ct += 1
                if ct >= n:
                    return True
        return ct >= n        

sol=Solution()

print(sol.canPlaceFlowers( [1,0,0,0,1],  1))#true
print(sol.canPlaceFlowers( [1,0,0,0,1],  2))#false
print(sol.canPlaceFlowers( [0,0,1,0,1],  1))#true

