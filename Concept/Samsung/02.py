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
#sys.stdin = open("input.txt", "r")
sys.stdin = open("Samsung/02sample_input.txt", "r") # test code

T = int(input())

"""
    test case 1)
    [input]
    3 3 2 4 << #.model, r, b, y
    1 1 1   << #.1 필요 전구 수
    1 0 2   << #.2
    1 1 0   << #.3
    [output] 3
"""
def solution(n, red, blue, yellow, models):
    # 장식 조명 모델 별 최대 생산 가능 개수:3
    # TC O(4**n) SC O(n)
    res = 0

    def backtracking(idx, cntR, cntB, cntY, total):
        nonlocal res

        if idx == n:
            res = max(res, total)
            return
        
        r, b, y = models[idx]

        for i in range(4):
            if (cntR+i*r <= red and cntB+i*b <= blue and cntY+i*y <= yellow):
                backtracking(idx+1, cntR+i*r, cntB+i*b, cntY+i*y, total+i)

    backtracking(0,0,0,0,0)
    return res

def optimal_solution(n, red, blue, yellow, models):
    # 장식 조명 모델 별 최대 생산 가능 개수:3
    # TC O(nlogn) SC O(n)
    counts = []
    for r, b, y in models:
        max_r = red//r if r > 0 else 3
        max_b = blue//b if b>0 else 3
        max_y = yellow//y if y>0 else 3

        max_count = min(3, max_r, max_b, max_y)
        
        total = (r+b+y) if (r+b+y) > 0 else 1
        counts.append((max_count, r, b, y, total))
    
    counts.sort(reverse=True, key=lambda x:(x[0], -x[4]))

    res = 0
    for max_count, r, b, y, _ in counts:
        make = min(max_count, 
                   red//r if r > 0 else max_count,
                    blue//b if b>0 else max_count,
                    yellow//y if y>0 else max_count)
        
        res += make
        red -= (make*r)
        blue -= (make*b)
        yellow -= (make*y)
    
    return res


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, red, blue, yellow = map(int, input().split())
    models = []
    for _ in range(n):
        r, p, y = map(int, input().split())
        models.append((r, p, y))

    res = solution(n, red, blue, yellow, models)
    print(f"#{test_case} {res}")
    # ///////////////////////////////////////////////////////////////////////////////////
