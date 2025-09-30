class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)-1
        ans, A=nums[0], 1
        for k in range(1, n+1):
            A=A*(n-k+1)//k
            ans=(ans+nums[k]*A)%10
        return ans
        