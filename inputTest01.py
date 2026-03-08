# 1. 사용자로부터 이름과 나이 입력받기
name = input("이름을 입력하세요: ")
# 2. 나이를 입력받아 정수형으로 형변환하기
age = int(input("나이를 입력하세요: "))


# 2. 결과 출력 (f-string 활용)
print(f"{name}님의 나이는 {age}세 입니다.")
print(type(name),type(age))

