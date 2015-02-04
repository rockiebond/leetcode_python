class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        processed={}
        for i in range(0,len(num)):
            if target-num[i] in processed:
                return [processed[target-num[i]]+1,i+1]
            processed[num[i]]=i
solution=Solution()
result=solution.twoSum([1,3,5,7,3],6)
print result

