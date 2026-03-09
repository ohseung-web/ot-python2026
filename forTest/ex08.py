target = int(input('목표 일 매출액: '))

total_sales = 0
achieve_cnt = 0
max_sales = -1
min_sales = -1
max_day = ''
min_day = ''

for i in range(1, 8):
    if i == 1:   day = '월요일'
    elif i == 2: day = '화요일'
    elif i == 3: day = '수요일'
    elif i == 4: day = '목요일'
    elif i == 5: day = '금요일'
    elif i == 6: day = '토요일'
    else:        day = '일요일'

    sales = int(input(f'{day} 매출: '))
    total_sales += sales

    if max_sales == -1 or sales > max_sales:
        max_sales = sales
        max_day = day
    if min_sales == -1 or sales < min_sales:
        min_sales = sales
        min_day = day

    if sales >= target:
        print(f'  →  목표 달성')
        achieve_cnt += 1
    elif sales >= target * 0.7:
        print(f'  →  분발 필요')
    else:
        print(f'  →  목표 미달')

avg = total_sales // 7
print(f'총 매출: {total_sales:,}원  |  일평균: {avg:,}원')
print(f'최고 매출: {max_day} {max_sales:,}원  |  최저 매출: {min_day} {min_sales:,}원')
print(f'목표 달성: {achieve_cnt}일')
