class Solution:
    def moveZeroes(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                # if it is a non zero at r, swap with the element at l
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

def main():
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)

if __name__ == "__main__":
    main()
