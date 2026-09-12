class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter="#"
        res=""
        for s in strs:
            res+=str(len(s))+delimiter+s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        delimiter="#"
        
        numberStartPointer=0
        iterPointer=0
        result=[]

        while iterPointer<len(s):
            char=s[iterPointer]
            if char == delimiter:
                decodingStrLen = int(s[numberStartPointer:iterPointer])
                numberStartPointer = iterPointer+1+ decodingStrLen
                decodedStr = s[iterPointer+1:numberStartPointer]
                result.append(decodedStr)
                iterPointer = numberStartPointer
            iterPointer+=1
            
        return result
