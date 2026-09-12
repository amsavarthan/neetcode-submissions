class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        for s1 in s:
            map[s1]=map.get(s1,0)+1

        for t1 in t:
            map[t1]=map.get(t1,0)-1
        
        flag=True
        for value in map.values():
            if value != 0:
                flag=False
                break
                
        return flag

