# 1. 두 개의 값을 입력받기
# input()은 문자로 받으므로 바로 int()를 씌워 숫자로 바꿉니다.
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 2. 사칙연산 수행
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

# 3. 결과 출력 (서식 문자를 활용하여 깔끔하게 표시)
print("-" * 30)
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} / {num2} = {div}")
print("-" * 30)