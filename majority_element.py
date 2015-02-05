class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dic = {}
        leng = len(num)
        for i in range(0, leng):
            if num[i] not in dic:
                dic[num[i]] = 1
            else:
                dic[num[i]] = dic[num[i]]+1

            if dic[num[i]] > leng/2:
                return num[i]
solution = Solution()
num = [1, 2, 3, 4, 4, 5, 4, 4]
print solution.majorityElement(num)
