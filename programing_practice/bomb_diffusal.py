class Solution: 
    def difffuse(self,code: list[int], k : int) -> [int]:
        n = len(code)
        result= []
        if k > 0:
            for i in range(0,n):
                sum = 0
                for j in range (i+1,i+k+1):
                    sum += code[j % n]
                result.append(sum)
        if k < 0:
            for i in range(0,n):
                sum = 0
                for j in range(i-1,i+k-1,-1):
                    sum += code[j % n]
                result.append(sum)
        elif k == 0:
            for i in range(0,n):
                result.append(0)
        
        return result
            


code = [5,7,1,4]
k = 3

sol = Solution()
sol.difffuse(code,k)
print(sol)