"""
    given array, return minimum rows
        if [5, 4, 3, 2, 6, 1]
        [5, 4, 3, 2], [6, 1] => 2
    arr[-1] > current number
"""

def solution(arr):
    # O(n*m), O(m)
    res = []

    for num in arr:
        flag = True
        for i in range(len(res)):
            if res[i] > num:
                res[i] = num
                flag = False
                break
        if flag:
            res.append(num)
    # print(res)
    return len(res)

import bisect
def optimal_solution(arr):
    # binary search O(n*logm), O(m)
    res = []

    for num in arr:
        idx = bisect.bisect_right(res, num)
        # print(idx)
        if idx < len(res):
            res[idx] = num
        else:
            res.append(num)
        # print(res)
    return len(res)

arr = [[5, 4, 3, 2, 6, 1], [4, 5, 9, 8]]
for a in arr:
    print(optimal_solution(a))
