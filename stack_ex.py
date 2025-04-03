#stack_ex
#queue_ex

from queue import LifoQueue

q = LifoQueue()
numbers = [2,7,10,2,1,-4,15]
for number in numbers:
 q. put (number) #put array into lifo.q 
 # q.get method in queue - always gets you the latest's next item in queue


class Solution :
    def SumFx (self , q:LifoQueue )-> int:
        sum1=0
        
        while not q.empty():
           sum1+=q.get()
        return(sum1)
        
    def MultFx (self , q:LifoQueue )-> int:
        msum1=1
        
        while not q.empty():
           msum1*=q.get()
           
        return(msum1)      
    
    def SumOdd_Fx (self , q:LifoQueue )-> int:
        sosum1=0
        #Oddnum=[]
        
        while not q.empty():
           gotnext=q.get()
           if gotnext % 2 != 0 :
              #Oddnum.append(gotnext)
             # for i in Oddnum :
            #     q.put(i)
            sosum1+=gotnext
        return(sosum1)  
        
    def Sum3rd_Fx (self , q:LifoQueue )-> int:
        sum3=0
        diff3rd=0
        while not q.empty():
           
           cur_valinque=q.get()

           diff3rd+=1

           if diff3rd%3==0:

            sum3 +=cur_valinque

        return(sum3)      

sol=Solution()
   
# HERE: Create new queues for each method call to avoid modifying the original queue
q_sum = LifoQueue()
q_mult = LifoQueue()
q_odd = LifoQueue()
q_3rd = LifoQueue()
for num in numbers:
    q_sum.put(num)
    q_mult.put(num)
    q_odd.put(num)
    q_3rd.put(num)

ans_sum = sol.SumFx(q_sum)
ans_msum = sol.MultFx(q_mult)
ans_odsum = sol.SumOdd_Fx(q_odd)
ans_3rdsum = sol.Sum3rd_Fx(q_3rd)

# Print the results
print ('Therefore , from SumFx , the Sum will be : ' , ans_sum )#33
print ('And for multiplication , the Product will be : ' , ans_msum )#-16800 
print ('for Odd Sum : ' , ans_odsum )#23
print ('for Every 3rd values Sum : ' , ans_3rdsum )#6


            


