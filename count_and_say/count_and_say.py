class Solution:
    # @return a string
    def countAndSay(self,n):
        result='1'
        while n>1:
            result=self.doCount(result)
            n-=1
        return result

    def doCount(self,n):
        strNum=str(n)
        tmpNum=-1
        counter=0
        result =''
        for i in range(0,len(strNum)):
            if tmpNum==-1:
                tmpNum=strNum[i]
                counter=1
            elif tmpNum==strNum[i]:
                counter=counter+1
            else:
                result=result+str(counter)+str(tmpNum)
                tmpNum=strNum[i]
                counter=1
        result=result+str(counter)+str(tmpNum)
        return result
