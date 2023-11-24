# input array 2,1,5,3 and target = 4 so function should return 1,3

# Method 1 - Brute Force O(n^2)
def twoSum(arr, target):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                return i, j
    return None


# Method2 - O(n)
# check if t-val exiists in hashmap, return that index and current, else put that in hashmap
def twoSum2(arr, target):
    # an empty hashmap
    hashmap = {}
    for idx, val in enumerate(arr):
        diff = target - val
        if diff in hashmap:
            # return a pair of that index found and current
            return [hashmap[diff], idx]
        # add it in hashmap
        hashmap[val] = idx


# Calling the function
result = twoSum2([2, 1, 5, 3], 4)
print(result)
