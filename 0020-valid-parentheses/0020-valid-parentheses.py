class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        l=[]
        l.append(s[0])
        for i in range(1,len(s)):
            # print(l)
            if s[i] == '}' and (len(l)==0 or l[-1]!='{'):
                if(len(l)>0):
                    l.pop()
                return False
            elif (s[i] == '}' and l[-1]=='{'):
                if(len(l)>0):
                    l.pop()
            if s[i] == ']' and (len(l)==0 or l[-1]!='['):
                if(len(l)>0):
                    l.pop()
                return False
            elif (s[i] == ']' and l[-1]=='['):
                if(len(l)>0):
                    l.pop()
            if s[i] == ')' and (len(l)==0 or l[-1]!='('):
                if(len(l)>0):
                    l.pop()
                return False
            elif (s[i] == ')' and l[-1]=='('):
                if(len(l)>0):
                    l.pop()

            if s[i] in ['(','{','[']:
                l.append(s[i])
        # print(l)
        if len(l)==0:
            return True
        return False

                
            