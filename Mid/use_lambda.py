class Student:
    def __init__(self, name, write, english, math):
        self.name = name
        self.write = write
        self.english = english
        self.math = math


n = int(input())

arr = [
    tuple(input().split())
    for _ in range(n)
]
children = [Student(name, int(write), int(english), int(math)) for name, write, english, math in arr]

# 각 과목당 총점의 합으로 오름차순으로 정렬하기
children.sort(key=lambda x: (x.write + x.english + x.math))

for child in children:
    print(child.name, child.write, child.english, child.math)


