# 클래스 선언하기
# 클래스 선언시 첫글자는 대문자로 하는것이 관용적

class Product:
    def __init__(self,name,code):
        self.name = name
        self.code = code

# 선언해준 클래스를 사용해보기

product1 = Product('codetree',50)

print(f"상품의 이름은 : {product1.name}입니다. 코드는 : {product1.code} 입니다. ")

# 만약 코드를 입력을 받는다면!?
# 숫자로 입력받는 코드의 경우 int형으로 입력을 받자

product_id2,code2 = input().split()
product2 = Product(product_id2,int(code2))

print(f"상품의 이름은 : {product2.name}입니다. 코드는 : {product2.code} 입니다. ")
