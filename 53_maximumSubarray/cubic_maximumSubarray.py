
from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_sum = float('-inf')  # smallest number

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray_sum = 0
            for k in range(i, j + 1):  # (j+1 inclusive meaning from i to j)
                subarray_sum += nums[k]  # Add each element to the subarray sum
            if subarray_sum > max_sum:
                max_sum = subarray_sum

    return max_sum


result = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("Maximum Subarray Sum:", result)
