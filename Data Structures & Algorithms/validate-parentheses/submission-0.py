class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if(len(stack)==0):
                stack.append(s[i])
            else:
                prev = stack[len(stack)-1]
                curr = s[i]

                if (prev =="(" and curr==")") or (prev =="[" and curr=="]") or (prev =="{" and curr=="}"):
                    stack.pop()
                else:
                    stack.append(curr)
        
        return len(stack)==0