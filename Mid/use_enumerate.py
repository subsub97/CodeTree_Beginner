class Student:
    def __init__(self,kor,eng,math,number):
        self.kor = kor
        self.eng = eng
        self.math = math
        self.rank = rank


students = [
    Student(80,10,20,1),
    Student(90,70,30,2),
    Student(60,20,50,3),
]

#국어 점수를 기준으로 정렬
students.sort(key = lambda x: -x.kor)

''' sort를 이용해서 정렬된 배열을 등수와 함께 출력하기 위해서
    단순 for문이 아닌 enumerate를 이용하여 출력함 '''

for idx, student in enumerate(students, start =1):
    print(f"{idx}등: {student.rank}번")