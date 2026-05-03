class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sh={}
        th={}
        if len(t)!=len(s):
            return False
        for i in range(len(t)):
            sh[s[i]]=1+sh.get(s[i],0)
            th[t[i]]=1+th.get(t[i],0)
        return sh==th
        