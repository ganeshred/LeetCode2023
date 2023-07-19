class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        # s1=re.sub(r'\W+', '', s)
        s1 = re.sub('[^A-Za-z0-9]', '', s)
        n=len(s1)
        s1=s1.lower()
        print(s1)
        for i in range(len(s1)):
            if s1[i] != s1[n-1-i]:
                return False
        return True