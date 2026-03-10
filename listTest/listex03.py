# 주문 데이터 (리스트 안에 딕셔너리)
orders = [
    {'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
    {'id': 2, 'product': '마우스', 'amount': 35000, 'status': 'PENDING'},
    {'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
    {'id': 4, 'product': '키보드', 'amount': 89000, 'status': 'CANCELLED'},
    {'id': 5, 'product': '웹캠', 'amount': 75000, 'status': 'PAID'}
]

# 결제 완료된 주문을 저장할 새로운 리스트
paid_orders = []

# 주문 리스트를 하나씩 확인
for order in orders:
    
    # 주문 상태가 PAID이면
    if order['status'] == 'PAID':
        
        # paid_orders 리스트에 추가
        paid_orders.append(order)


# -----------------------------
# 결제 완료 주문 출력
# -----------------------------

print('=== 결제 완료 주문 ===')

# 총 결제 금액을 저장할 변수
total = 0

# 결제 완료 주문을 하나씩 출력
for order in paid_orders:

    # 주문 정보 출력
    # print(str(order['id']) + '번 주문 / 상품: ' + order['product'] + ' / 금액: ' + str(order['amount']) + '원')
    print(f"{str(order['id'])} 번 주문 / 상품: {order['product']} / 금액: {order['amount']:,}원" )
    
    # 총 금액 계산
    total = total + order['amount']


# 전체 결제 금액 출력
# print('\n총 결제 금액: ' + str(total) + '원')
print(f"\n총 결제 금액:{total:,}원")




# # 주문 데이터
# orders = [
#     {'id': 1, 'product': '노트북',  'amount': 1200000, 'status': 'PAID'},
#     {'id': 2, 'product': '마우스',  'amount':   35000, 'status': 'PENDING'},
#     {'id': 3, 'product': '모니터',  'amount':  450000, 'status': 'PAID'},
#     {'id': 4, 'product': '키보드',  'amount':   89000, 'status': 'CANCELLED'},
#     {'id': 5, 'product': '웹캠',    'amount':   75000, 'status': 'PAID'},
# ]
 
# # PAID 주문 필터링
# paid_orders = [o for o in orders if o['status'] == 'PAID']
 
# # 금액 내림차순 정렬
# paid_orders.sort(key=lambda o: o['amount'], reverse=True)
 
# print('=== 결제 완료 주문 (금액 순) ===') 
# total = 0
# for o in paid_orders:
#     print(f"  #{o['id']} {o['product']}: {o['amount']:,}원")
#     total += o['amount']
 
# print(f'\n총 결제 금액: {total:,}원')
