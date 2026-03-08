# 1. 변수에 데이터 저장하기 (서식 문자에 넣을 재료들)
order_no = "1078718855"
addr = "서울시 종로구 종로3가"
name = "김사장"
phone = "070-1234-5678"

# 품목 데이터
item1 = "블루투스 이어폰"
p1 = 85000
q1 = 1

item2 = "USB3.0 8G"
p2 = 8000
q2 = 1

# 금액 계산 (간단한 산술 연산)
amt1 = p1 * q1
amt2 = p2 * q2
total = amt1 + amt2
received = 100000
change = received - total

# 2. 영수증 출력 (배운 내용만 활용)
print("          파이썬 쇼핑몰") # 공백으로 대략 중앙 맞춤
print("번호 : %s" % order_no)
print("주소 : %s" % addr)
print("성명 : %s" % name)
print("전화 : %s" % phone)
print("-" * 50)

# 헤더 부분 (이스케이프 \t 활용)
print("품명\t\t\t단가\t수량\t금액")
print("-" * 50)

# 품목 출력 (서식 문자 % 활용하여 줄 맞추기)
# %-20s : 20칸 왼쪽 정렬 / %10d : 10칸 오른쪽 정렬
print("%-20s %10d %5d %10d" % (item1, p1, q1, amt1))
print("%-20s %10d %5d %10d" % (item2, p2, q2, amt2))
print("-" * 50)

# 하단 결제 정보
print("소 계 %38d" % total)
print("-" * 50)
print("청구금액 %35d" % total)
print("받은금액 %35d" % received)
print("거스름돈 %35d" % change)
print("-" * 50)