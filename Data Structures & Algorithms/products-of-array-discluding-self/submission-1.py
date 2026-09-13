class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Base idea - split by index [s:i + i+1:e] to get the part before and after it
        # calculate the product and store in array.
        # This will be O(n^2) since we multiply after split.

        # lets precalculate prefix and suffix for each index. multiply both to get ans

        prefixProduct=[]
        suffixProduct=[]

        for i in range(len(nums)):
            if i==0:
                prefixProduct.append(1)
            else:
                prevNum = nums[i-1]
                lastPrefix = prefixProduct[len(prefixProduct)-1]
                prefixProduct.append(lastPrefix*prevNum)

        for i in reversed(range(len(nums))):
            if i==len(nums)-1:
                suffixProduct.append(1)
            else:
                prevNum = nums[i+1]
                lastSuffix = suffixProduct[len(suffixProduct)-1]
                suffixProduct.append(lastSuffix*prevNum)

        suffixProduct = list(reversed(suffixProduct))

        return [prefixProduct[i] * suffixProduct[i] for i in range(len(nums))]