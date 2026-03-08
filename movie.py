# 데이터 설정
ticket_no = "2026-0309-01"
movie = "파이썬의 습격"
time = "14:30 ~ 16:10"

# 금액 및 계산
p1, q1 = 15000, 2
p2, q2 = 10000, 1
total = (p1 * q1) + (p2 * q2)

# 출력
print("=" * 50)
print(f"{'PYTHON CINEMA':^50}")
print("=" * 50)
print(f"티켓번호 : {ticket_no}")
print(f"상영관   : 7관 (4층)")
print(f"영화명   : {movie}")
print(f"상영시간 : {time}")
print("-" * 50)
print(f"{'구분':<15} {'단가':>10} {'인원':>5} {'금액':>10}")
print("-" * 50)
print(f"{'일반 성인':<15} {p1:>10,} {q1:>7} {p1*q1:>10,}")
print(f"{'청소년':<15} {p2:>10,} {q2:>7} {p2*q2:>10,}")
print("-" * 50)
print(f"{'총 결제 금액':<38} {total:>10,}")
print("=" * 50)

print(type(p1))