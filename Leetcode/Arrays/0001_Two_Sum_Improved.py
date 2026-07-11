class Solution:
    def twoSum(self, nums, target):

        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))

        arr.sort()

        smallest = 0
        largest = len(arr) - 1

        while smallest < largest:

            total = arr[smallest][0] + arr[largest][0]

            if total == target:
                return [arr[smallest][1], arr[largest][1]]

            elif total > target:
                largest -= 1

            else:
                smallest += 1

        return []