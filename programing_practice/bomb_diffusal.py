class Solution: 
    def difffuse(self,code: list[int], k : int) -> [int]:
        n = len(code)
        result= []
        if k >= 0:
            print('Run formward loop')
            for i in range(0,n):
                sum = 0
                for j in range (i+1,i+k+1):
                    sum += code[j % n]
                result.append(sum)
            print(result)
                    
        if k <= 0:
            print('Run backward loop')
            for i in range(0,n):
                sum = 0
                for j in range(i-1,i+k-1,-1):
                    sum += code[j % n]
                result.append(sum)
            print(result)
            # return code[i] == sum
            # if k == 0:
            #     print('replace with 0') 
            #     pass
            # result.append(sum)


code = [5,7,1,4]
k = -3

sol = Solution()
sol.difffuse(code,k)
print(sol)