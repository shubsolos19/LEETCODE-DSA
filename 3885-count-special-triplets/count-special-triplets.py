class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        total = Counter(nums)
        left = Counter()
        cnt = 0
        mod = 10**9 + 7
        for n in nums:
            target = n * 2
            total[n] -= 1
            l = left.get(target, 0)
            r = total.get(target, 0)
            if l >= 1 and r >= 1:
                cnt = (cnt + l * r) % mod
            left[n] += 1
        return cnt