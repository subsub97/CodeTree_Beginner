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

'''
list comprehension을 이용 할 때 
조건을 넣어서 이용 할 수 있다.
ex ) 
arr_3 = [
[ 1 if arr_1[i][j] != arr_2[i][j] else 0 for j in range(m)]
for i in range(n)
]

위 코드처럼 if else 문을 이용하여 어떠한 것을 추가할지 정해줄 수 있다.

'''