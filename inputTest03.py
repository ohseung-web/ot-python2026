# 1. 사용자로부터 이름, 키, 체중 입력받기
name = input("이름을 입력하세요: ")
height = float(input("키를 입력하세요(cm): "))  # 계산을 위해 실수로 변환
weight = float(input("현재 체중을 입력하세요(kg): "))

# 2. 비만도 계산 수행
# 표준 체중 = (현재 키 - 100) * 0.9
standard_weight = (height - 100) * 0.9

# 비만도(%) = 현재 체중 / 표준 체중 * 100
obesity = (weight / standard_weight) * 100

# 3. 결과 출력 (소수점 2자리까지 표시)
print("-" * 40)
# f-string의 :.2f 또는 % 서식의 %.2f를 활용합니다.
print(f"{name}님의 비만도는 {obesity:.2f}% 입니다.")
print("-" * 40)