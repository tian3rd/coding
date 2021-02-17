#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        print(self.nums)

    def add(self, val: int) -> int:
        self.insertval(val)
        # print(self.nums)
        return self.nums[-self.k]
        
    def insertval(self, val: int):
        if self.nums == []:
            self.nums.append(val)
        low, high = 0, len(self.nums)-1
        while low<=high:
            mid = (low+high)//2
            if self.nums[mid] == val:
                self.nums.insert(mid, val)
                # must return, or infinite loop
                return
            elif self.nums[mid] < val:
                low = mid+1
            else:
                high = mid-1
        if low>high:
            self.nums.insert(low, val)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

