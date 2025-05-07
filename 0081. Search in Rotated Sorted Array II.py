def search(nums, target):
    def binary_search(start, finish):
        if start > finish:
            return finish

        middle = (start + finish) // 2
        if nums[start] == nums[middle] == nums[finish] and start != finish:
            index = binary_search(start, middle - 1)
            if nums[index] == target:
                return index
            else:
                return binary_search(middle + 1, finish)
        else:
            if nums[middle] <= target:
                if nums[middle] <= nums[finish]:
                    if target <= nums[finish]:
                        return binary_search(middle + 1, finish)
                    else:
                        return binary_search(start, middle - 1)
                else:
                    return binary_search(middle + 1, finish)
            else:
                if nums[middle] <= nums[finish]:
                    return binary_search(start, middle - 1)
                else:
                    if target <= nums[finish]:
                        return binary_search(middle + 1, finish)
                    else:
                        return binary_search(start, middle - 1)

    return nums[binary_search(0, len(nums) - 1)] == target