class Solution:
    # @return a boolean
    def isValid(self,s):
        stack=[]
        for i in range(0,len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            if len(stack)==0:
                return False
            if s[i]==')' and stack.pop()!='(':
                return False
            if s[i]==']' and stack.pop()!='[':
                return False
            if s[i]=='}' and stack.pop()!='{':
                return False
        if len(stack)>0:
            return False
        return True
solution=Solution()
print solution.isValid('[')
                
