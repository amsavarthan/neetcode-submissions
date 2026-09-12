class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        for s1 in s:
            if s1 in map:
                map[s1]+=1
            else:
                map[s1]=1

        for t1 in t:
            if t1 in map:
                map[t1]-=1
            else:
                map[t1]=-1
        print(map)
        flag=True
        for value in map.values():
            if value != 0:
                flag=False
                break
        return flag

