#lcsw_134_GasStation
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station_ct=0
        testing_each=0
        sum_for_all=0
        for i in range(len(gas)):
            testing_each+= gas[i]-cost[i]
            sum_for_all+= gas[i]-cost[i]
            if testing_each < 0 :
                station_ct = i + 1
                testing_each=0
        if sum_for_all >= 0:
            return station_ct 
        else:
            return -1

                
        
            
  



sol=Solution()
print(sol.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1]))

# print(sol.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
# print(sol.canCompleteCircuit([2,3,4],[3,4,3]))

