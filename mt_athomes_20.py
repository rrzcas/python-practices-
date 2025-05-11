# mt_athomes_20
from dateutil import parser

def total_elapsed_time(L):
    """ L is a list of tuples (e1, e2) where:
        e1 and e2 are strings representing a date and time. e.g. '9/30/2021 1:35 PM'
        e2 occurs later in time than e1
    Consider the elapsed time for a tuple to be the difference between e2 and e1.
    Returns the sum of all the elapsed times, in seconds, in L. """
    td_sum=0
    for i in L:
        e1 =parser.parse(i[0])
        e2 = parser.parse(i[1])


        td_sum += (e2-e1).total_seconds()    
    return td_sum
t1 = '1/1/2021 2:00 PM'
t2 = '1/1/2021 2:05 PM'
t3 = '3/12/2021 1:22 PM'
t4 = '3/12/2021 1:32 PM'
t5 = '7/13/2021 6:00 PM'
t6 = '7/13/2021 6:02 PM'
L = [(t1, t2), (t3, t4), (t5, t6)]  # 5min + 10min + 2min = 1020 sec
print(total_elapsed_time(L))    # prints 1020
    
