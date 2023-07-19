class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s)!=len(goal):
            return False
         
        l=Counter(s)
        r=Counter(goal)


        if l != r:
            return False

        diff=0

        for i in range(len(s)):
            if s[i]!=goal[i]:
                diff+=1        
        
        if diff == 2:
            return True

        if diff==0 and s==goal and len(set(s)) < len(s):
            return True
        
        return False

        

        
