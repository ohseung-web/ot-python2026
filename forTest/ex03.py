select_cnt = 0
insert_cnt = 0
update_cnt = 0
delete_cnt = 0

while True:
    query = input('쿼리 유형 입력: ').upper()

    if query == 'SELECT':
        select_cnt += 1
    elif query == 'INSERT':
        insert_cnt += 1
    elif query == 'UPDATE':
        update_cnt += 1
    elif query == 'DELETE':
        delete_cnt += 1
    elif query == 'REPORT' or query == 'EXIT':
        total = select_cnt + insert_cnt + update_cnt + delete_cnt
        print('--- 쿼리 실행 현황 ---')
        print(f'SELECT : {select_cnt}회')
        print(f'INSERT : {insert_cnt}회')
        print(f'UPDATE : {update_cnt}회')
        print(f'DELETE : {delete_cnt}회')
        print(f'총 실행 : {total}회')
        if total > 0 and select_cnt / total >= 0.7:
            print('SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.')
        if query == 'EXIT':
            break
    else:
        print('알 수 없는 쿼리 유형입니다.')
