class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        zero=-math.inf
        one=-math.inf
        result=-math.inf
        for i in range(len(arr)):
            one=max(arr[i],one+arr[i],zero)
            zero=max(arr[i],zero+arr[i])
            result=max(result,one,zero)
        return result
        