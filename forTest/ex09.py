check1  = 'DB 마이그레이션 완료 여부'
check2  = 'application-prod.properties 설정 확인'
check3  = 'JWT Secret Key 변경 여부'
check4  = 'CORS 허용 도메인 설정 완료'
check5  = 'API 엔드포인트 테스트 통과'

fail_cnt  = 0
fail_nums = ''
fail_names = ''

for i in range(1, 6):
    if i == 1:   item = check1
    elif i == 2: item = check2
    elif i == 3: item = check3
    elif i == 4: item = check4
    else:        item = check5

    while True:
        ans = input(f'[{i}/5] {item} (Y/N): ').upper()
        if ans == 'Y' or ans == 'N':
            break
        print('  Y 또는 N 으로 입력하세요.')

    if ans == 'N':
        print('  → 미완료')
        fail_cnt += 1
        fail_nums  = fail_nums  + str(i) + ','
        fail_names = fail_names + item + ','
    else:
        print('  → 완료')

if fail_cnt == 0:
    print('배포 승인! 배포를 진행하세요.')
else:
    print(f'배포 보류! {fail_cnt}개 항목을 해결 후 재시도하세요.')
    # 미통과 항목 출력 (for + split 대신 while로 파싱)
    nums  = fail_nums[:-1]   # 마지막 쉼표 제거
    names = fail_names[:-1]
    n_idx = 0
    v_idx = 0
    for k in range(fail_cnt):
        # 쉼표 위치 찾아 잘라내기
        n_end = nums.find(',', n_idx)
        v_end = names.find(',', v_idx)
        if n_end == -1: n_end = len(nums)
        if v_end == -1: v_end = len(names)
        num_str  = nums[n_idx:n_end]
        name_str = names[v_idx:v_end]
        print(f'  · [{num_str}] {name_str}')
        n_idx = n_end + 1
        v_idx = v_end + 1
