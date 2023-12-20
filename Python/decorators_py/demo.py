from math import isnan

from math import isnan
from cmath import nan




def max_count(a):
    if len(a) == 0:
        return 0
    else:
        count_store = []
        count = 0
        
        for i in a:
            if isnan(i) == True:
               count += 1
            else:
                count_store.append(count)
                count = 0

        return max(count_store)


# a = [nan, nan, nan, 0.1, nan, 0.16, 1, 0.16, 0.101, nan]
a=[]
# print(type(nan))
print(max_count(a))
# max_count(a)

    #  def count_further(count,i):
    #         if isnan(a[i+1]) == True:
    #         count += 1
    #         i
    #         count_further(count,i+1)
    #     else :
    #         i
    #         count_store.append(count)
    #         i += 1
    #         return i
        # return count