def solutions(heights):
    mx = 0
    ans = []

    for i in range(len(heights)-1, -1, -1):
        if heights[i] > mx:
            mx = max(mx, heights[i])
            ans.append(i)

    ans.reverse()
    return ans

heights = [4,2,3,1]
print(solutions(heights))
