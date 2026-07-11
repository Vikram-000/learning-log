def twoSum(self, nums, target):

    current = []
    for i in range(len(nums)):
        current.append((nums[i], i))

    while current:

        largest = max(current)
        largest_value = largest[0]
        largest_index = largest[1]

        needed = target - largest_value

        for value, index in current:
            if value == needed and index != largest_index:
                return [largest_index, index]

        current.remove(largest)

        new_current = []
        for value, index in current:
            if value > needed:
                new_current.append((value, index))

        current = new_current

    return []