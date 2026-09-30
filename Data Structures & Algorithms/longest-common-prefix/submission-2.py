class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare=strs[0]
        prefixLength=len(compare)

        for i in range(1,len(strs)):
            curr = strs[i]
            currIterPrefixLength =0
            for j in range(min(len(curr),len(compare))):
                if curr[j] != compare[j]:
                    break;
                currIterPrefixLength+=1
            prefixLength=min(prefixLength,currIterPrefixLength)

        return compare[:prefixLength]
