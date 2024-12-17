def solution(s):
    stack = []
    stack.append(0)

    for c in s:
        if c == "(":
            stack.append(0)
        else:
            tmp = stack[-1]
            stack = stack[:-1]

            val = 0
            if tmp >0:
                val = 2*tmp
            else:
                val = 1
            
            stack[-1] += val

    return stack[-1]

S = "(()(()))"
print(solution(S))
