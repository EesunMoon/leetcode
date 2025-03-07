# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
import sys
from collections import Counter
#sys.stdin = open("input.txt", "r")
sys.stdin = open("Samsung/03sample_input.txt", "r") # test code
"""
    5           << 테스트 개수
    18211 0 3   << Bi, Ci, Di
    29790 1 1
    31307 2 1
    22294 0 1
    28334 0 3
    
    output: 3

    ## 3 0 2 1 9452
"""

T = int(input())

def isMaching(A, B, C, D):
    strA, strB = str(A), str(B)

    # Ci 계산
    countC = 0
    remainA, remainB = [], []
    for i in range(5):
        if strA[i] != strB[i]:
            remainA.append(strA[i])
            remainB.append(strB[i])
        else:
            countC += 1
    
    if countC != C:
        return False
    
    # Di 계산
    countD = 0
    countA = {}
    for candA in remainA:
        countA[candA] = 1+ countA.get(candA, 0)
    
    for candB in remainB:
        if countA.get(candB, 0) != 0:
            countD += 1
            countA[candB] -= 1
    return countD == D

def optimal_isMatching(A, B, C, D):
    strA, strB = str(A), str(B)

    # Ci 계산
    countC = sum(1 for a, b in zip(strA, strB) if a == b)
    
    if countC != C:
        return False
    
    # total match 계산
    countA = Counter(strA)
    countB = Counter(strB)
    total = sum(min(countA[d], countB[d]) for d in countA)

    return (total-countC) == D

def solution(n, B, C, D):
    # C: A와 Bi의 각 자리를 비교할 때 일치하는 개수
    # D: C를 제외하고, 자리에 상관없이 일치하는 숫자 쌍의 개수
    # output: A가 될 수 있는 수의 개수 (A, Bi는 5자리 수)

    # A -> 10000~99999 모두 계산? O(89999n)
    #   -> [optimal] DFS로 possible candiate 생성
    res = 0
    for A in range(10000, 100000):
        flag = True
        for i in range(n):
            Bi, Ci, Di = B[i], C[i], D[i]
            if not optimal_isMatching(A, Bi, Ci, Di):
                flag = False
                break
        if flag:
            res += 1
    return res

def dfs(idx, curr):
    if idx == 5:
        A = int(curr)
        if all(optimal_isMatching(A, B, C, D) for B, C, D in lists):
            return 1
        return 0

    res = 0
    for digit in "0123456789":
        if idx == 0 and digit == "0":
            continue
        res += dfs(idx+1, curr+digit)
    return res

def optimal_solution(B, C, D):
    global lists
    lists = list(zip(B, C, D))

    return dfs(0, "")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    listB, listC, listD = [], [], []
    for _ in range(n):
        Bi, Ci, Di = map(int, input().split())
        listB.append(Bi)
        listC.append(Ci)
        listD.append(Di)

    # res = solution(n, listB, listC, listD)
    res = optimal_solution(listB, listC, listD)
    print(f"#{test_case} {res}")
    # ///////////////////////////////////////////////////////////////////////////////////
