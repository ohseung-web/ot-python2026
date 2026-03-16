# 1. 데이터 준비
order_no = "1078718855"
address = "서울시 종로구 종로3가"
name = "김사장"
phone = "070-1234-5678"

# 품목 데이터 (계산식 포함)
item1, p1, q1 = "블루투스 이어폰", 85000, 1
item2, p2, q2 = "USB3.0 8G", 8000, 1

amt1 = p1 * q1
amt2 = p2 * q2
total = amt1 + amt2
received = 100000
change = received - total

# 2. 출력 시작
print(f"{'파이썬 쇼핑몰':^45}") # ^45: 45칸 기준 가운데 정렬
print(f"번호 : {order_no}")
print(f"주소 : {address}")
print(f"성명 : {name}")
print(f"전화 : {phone}")
print("-" * 60)

# 헤더 (품명은 왼쪽, 나머지는 오른쪽 정렬)
# <20: 20칸 왼쪽 / >10: 10칸 오른쪽
print(f"{'품명':<20} {'단가':>10} {'수량':>5} {'금액':>10}")
print("-" * 60)

# 품목 출력 (:, 를 붙이면 천 단위 콤마가 자동으로 들어갑니다)
print(f"{item1:<20} {p1:>10,} {q1:>7} {amt1:>10,}")
print(f"{item2:<20} {p2:>10,} {q2:>7} {amt2:>10,}")
print("-" * 60)

# 하단 결제 정보
print(f"{'소 계':<45} {total:>10,}")
print("-" * 60)
print(f"{'청구금액':<43} {total:>10,}")
print(f"{'받은금액':<43} {received:>10,}")
print(f"{'거스름돈':<43} {change:>10,}")
print("-" * 60)

