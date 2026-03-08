# 1. C 스타일 (%) - 고전적인 방식
name = "공유"
age = 40
height = 184.5
print("이름: %s, 나이: %d세, 키: %.1fcm" % (name, age, height))

# 2. Python 3 (.format()) - 이미지에 나온 방식
# 정수, 실수, 진수 변환 활용
number = 255
print("10진수: {0}, 2진수: {0:b}, 16진수: {0:x}".format(number))
print("소수점 제한: {:.2f}".format(3.141592))

# 3. f-string (가장 권장되는 최신 방식)
# 변수명을 중괄호 안에 바로 넣어서 가독성이 좋습니다.
stock_name = "삼성전자"
price = 75000
print(f"현재 {stock_name}의 주가는 {price:6}원입니다.") # 6자리 고정 폭

# 4. 정렬 예제 (표 만들기)
print("\n--- 영수증 출력 예시 ---")
item1, price1 = "사과", 1500
item2, price2 = "포도", 30000
print(f"{item1:10} | {price1:6}원")
print(f"{item2:10} | {price2:6}원")