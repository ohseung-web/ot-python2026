# 거래 내역 (리스트 안에 리스트)
# [월, 매출금액]
# [월, 매출금액]
transactions = [
    ['2024-01', 3200000],
    ['2024-01', 1500000],
    ['2024-02', 2800000],
    ['2024-02', 900000],
    ['2024-03', 4100000],
    ['2024-03', 2200000],
    ['2024-04', 1800000],
    ['2024-04', 3300000],
    ['2024-05', 5000000],
    ['2024-06', 2100000]
]

# 월별 매출을 저장할 딕셔너리
monthly = {}

# 거래 내역을 하나씩 확인
for t in transactions:

    # 리스트에서 월과 금액 꺼내기
    month = t[0]      # 월
    amount = t[1]     # 매출 금액

    # 딕셔너리에 해당 월이 없으면 새로 생성
    if month not in monthly:
        monthly[month] = amount

    # 이미 있으면 매출을 더함
    else:
        monthly[month] = monthly[month] + amount


print('=== 월별 매출 ===')

# 월별 매출 출력
for month in monthly:
    print(f"{month} : {monthly[month]:,}원")


# ----------------------------
# 최고 매출 월 찾기
# ----------------------------

best_month = ''
best_sales = 0
first = True   # 첫 번째 데이터를 확인하기 위한 변수

for month in monthly:

    # 첫 번째 데이터라면 기준값으로 사용
    if first:
        best_sales = monthly[month]
        best_month = month
        first = False

    # 이후에는 더 큰 값이 있는지 비교
    elif monthly[month] > best_sales:
        best_sales = monthly[month]
        best_month = month


# ----------------------------
# 최저 매출 월 찾기
# ----------------------------

worst_month = ''
worst_sales = 0
first = True   # 첫 번째 데이터를 기준값으로 사용

for month in monthly:

    # 첫 번째 데이터라면 기준값으로 설정
    if first:
        worst_sales = monthly[month]
        worst_month = month
        first = False

    # 이후에는 더 작은 값이 있는지 비교
    elif monthly[month] < worst_sales:
        worst_sales = monthly[month]
        worst_month = month


# ----------------------------
# 평균 매출 계산
# ----------------------------

total = 0

# 전체 매출 합계 구하기
for month in monthly:
    total = total + monthly[month]

# 평균 계산
avg = total / len(monthly)


print()
print(f"최고 매출 월: {best_month} ({best_sales:,}원)")
print(f"최저 매출 월: {worst_month} ({worst_sales:,}원)")
print(f"월 평균 매출: {int(avg):,}원")



# # 거래 내역 (MySQL SELECT 결과라고 가정)
# transactions = [
#     ('2024-01', 3200000), ('2024-01', 1500000), ('2024-02', 2800000),
#     ('2024-02',  900000), ('2024-03', 4100000), ('2024-03', 2200000),
#     ('2024-04', 1800000), ('2024-04', 3300000), ('2024-05', 5000000),
#     ('2024-06', 2100000),
# ]
 
# # 월별 합산
# monthly = {}
# for month, amount in transactions:
#     monthly[month] = monthly.get(month, 0) + amount
 
# # 통계
# best_month  = max(monthly, key=lambda m: monthly[m])
# worst_month = min(monthly, key=lambda m: monthly[m])
# avg = sum(monthly.values()) / len(monthly)
 
# print('=== 월별 매출 ===') 
# for month, sales in sorted(monthly.items()):
#     rate = (sales - avg) / avg * 100
#     sign = '+' if rate >= 0 else ''
#     print(f'  {month}: {sales:,}원  ({sign}{rate:.1f}%)')
 
# print(f'\n최고 매출 월: {best_month}  ({monthly[best_month]:,}원)')
# print(f'최저 매출 월: {worst_month}  ({monthly[worst_month]:,}원)')
# print(f'월 평균 매출: {avg:,.0f}원')
