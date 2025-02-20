"""
    Brute Force: TC O(n**2) SC O(n)
    Optimal: prefix sum
        prefix(2) = sum(0~2)
        sum(1~2) = prefix(2) - prefix(0)
        nums [23, 2, 4, 7] k:6
        prefix [23, 25, 29, 36]
        module [5, 1, 5, 0]        
        sum(i~j) = prefix(j) - prefix(i-1) (i>0, i<j)
                = sum(0~j) - sum(0~i-1)
        => if there are same module result in module hashmap,
        the subsum between two variable 
"""
def has_good_subarray(nums, k):
    # prefix O(n) O(n)
    prefix = 0
    prefix_mod = {0:-1} # module: idx
    for i in range(len(nums)):
        prefix += nums[i]
        if prefix % k in prefix_mod:
            # check the subArray contain at least two element
            if i - prefix_mod[prefix%k] > 1:
                return True
        else:
            prefix_mod[prefix%k] = i
    return False
        
    # brute force O(n**2) O(n)
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subArray = nums[i:j+1]
            if sum(subArray) % k == 0:
                return True
    return False
    
    
# debug your code below
print(has_good_subarray([23, 2, 4, 7], 6))
