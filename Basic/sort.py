# sorted(arr) sorted 함수는 정렬된 함수를 출력하지만 arr에 변형을 만들지는 않는다.

# 변수명.sort() 함수는 반환값이 없다. ex) arr.sort 만으로도 정렬이 가능하다

# 오름차순 정렬

arr = [12, 47, 37, 81]
arr.sort()
print(arr)

arr = [12, 47, 37, 81]
arr = sorted(arr)
print(arr)


# 내림차순 정렬
arr = [12, 47, 37, 81]
arr.sort(reverse=True)
print(arr)

arr = [12, 47, 37, 81]
arr = sorted(arr, reverse=True)
print(arr)

# 문자열 sort

string = input()

# string.sort() 은 불가능

arr = list(string)
# print(arr)
arr.sort()
# print(arr)

print("".join(arr))

# sorted_str ="".join(arr)
# print(sorted_str)
