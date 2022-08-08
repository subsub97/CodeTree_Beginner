#2차원 배열을 만드는 것을 실습 해보자!

n = 3
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 2차원 배열에 값 넣기

num = 1
for i in range(n):
    for j in range(n):
        arr_2d[i][j] = num
        num += 2

# 출력하기 i,j 변수가 아닌 elem으로 출력하기

for row in arr_2d:
    for elem in row:
        print(elem,end = " ")

    print()