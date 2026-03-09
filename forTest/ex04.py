n = int(input('토큰 수를 입력하세요: '))
danger_cnt = 0
safe_cnt = 0

for i in range(1, n + 1):
    minutes = int(input(f'토큰 {i} 잔여시간(분): '))
    if minutes <= 0:
        print('[만료] 즉시 재발급 필요')
        danger_cnt += 1
    elif minutes <= 10:
        print('[위험] 곧 만료됩니다. 갱신 권장')
        danger_cnt += 1
    elif minutes <= 30:
        print('[주의] 만료가 가까워지고 있습니다.')
        danger_cnt += 1
    else:
        print('[정상] 유효한 토큰')
        safe_cnt += 1

print('--- 요약 ---')
print(f'정상 토큰: {safe_cnt}개 / 위험·만료 토큰: {danger_cnt}개')
