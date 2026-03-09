order_cnt = 0
total_price = 0
total_discount = 0

while True:
    grade = input('회원 등급 (END 종료): ').upper()
    if grade == 'END':
        break

    if grade not in ['BRONZE', 'SILVER', 'GOLD', 'VIP']:
        print('등록되지 않은 등급입니다.')
        continue

    price = int(input('구매금액: '))

    if grade == 'BRONZE':
        discount = 0
    elif grade == 'SILVER':
        discount = int(price * 0.05)
    elif grade == 'GOLD':
        discount = int(price * 0.10) + 5000
    else:  # VIP
        discount = int(price * 0.20) + 10000

    final = price - discount
    print(f'할인금액: {discount}원  →  결제금액: {final}원')

    order_cnt += 1
    total_price += price
    total_discount += discount

total_final = total_price - total_discount
print('--- 전체 주문 요약 ---')
print(f'주문 건수: {order_cnt}건')
print(f'총 구매금액: {total_price:,}원  |  총 할인: {total_discount:,}원  |  총 결제: {total_final:,}원')
