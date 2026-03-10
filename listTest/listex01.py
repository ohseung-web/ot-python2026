# # 상품 재고 관리
# 상품 이름 리스트
products = ['노트북', '마우스', '키보드', '모니터', '웹캠']

# 상품 재고 리스트
stocks = [15, 3, 8, 22, 5]

print('=== 재고 현황 ===')

# 리스트의 길이만큼 반복
for i in range(len(products)):

    # 상품 이름 가져오기
    product = products[i]

    # 재고 수량 가져오기
    stock = stocks[i]

    # 출력할 메시지 만들기
    # str(stock) => 숫자 stock를 문자열로 변경한다.
    msg = product + ': ' + str(stock) + '개'
    # 파이썬에서는 문자열과 숫자를 바로 더할 수 없습니다.
    # msg = product + ': ' + (stock) + '개'

    # 재고가 10개 미만이면 재고 부족 표시
    if stock < 10:
        msg = msg + ' 재고 부족'

    # 결과 출력
    print(msg)


# 전체 재고 계산
total = 0

# 재고 리스트를 하나씩 더하기
for stock in stocks:
    total = total + stock

print('\n전체 재고 합계:', total, '개')







# products = ['노트북', '마우스', '키보드', '모니터', '웹캠']
# stocks   = [15, 3, 8, 22, 5]
 
# print('=== 재고 현황 ===') 
# for product, stock in zip(products, stocks):
#     msg = f'{product}: {stock}개'
#     if stock < 10:
#         msg += '재고 부족'
#     print(msg)
 
# total = sum(stocks)
# print(f'\n전체 재고 합계: {total}개')
 
