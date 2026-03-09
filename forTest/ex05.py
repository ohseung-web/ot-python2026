n = int(input('측정 횟수: '))
total_time = 0
critical_cnt = 0
max_time = -1
min_time = -1

for i in range(1, n + 1):
    ms = int(input(f'응답시간 {i} (ms): '))
    total_time += ms

    # 최대/최소 갱신
    if max_time == -1 or ms > max_time:
        max_time = ms
    if min_time == -1 or ms < min_time:
        min_time = ms

    if ms <= 100:
        print('FAST')
    elif ms <= 300:
        print('NORMAL')
    elif ms <= 1000:
        print('SLOW')
    else:
        print('CRITICAL')
        critical_cnt += 1

avg = total_time / n
print(f'평균 응답시간: {avg:.1f}ms')
print(f'최대: {max_time}ms  |  최소: {min_time}ms')

if critical_cnt / n > 0.1:
    print('SLA 위반! 서버 점검이 필요합니다.')
