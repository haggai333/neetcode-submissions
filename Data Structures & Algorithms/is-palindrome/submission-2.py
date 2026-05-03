class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for i in s:
            if i.isalnum():
                a.append(i)
        l=0
        print(a)
        r=len(a)-1
        while r>=l:
            if a[l].lower()!=a[r].lower():
                return False
            r-=1
            l+=1
        return True
        