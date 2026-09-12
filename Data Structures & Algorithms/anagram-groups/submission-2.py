class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapOfMaps={}
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c)-ord('a')]+=1
            mapOfMaps[str(arr)]=mapOfMaps.get(str(arr),[])+[s]

        return list(mapOfMaps.values())
