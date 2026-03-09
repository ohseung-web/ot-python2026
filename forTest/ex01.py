code = int(input('상태코드를 입력하세요: '))

# 정확한 코드 판별
if code == 200:
    print('상태: 200 OK - 요청 성공')
elif code == 201:
    print('상태: 201 Created - 리소스 생성 성공')
elif code == 400:
    print('상태: 400 Bad Request - 잘못된 요청')
elif code == 401:
    print('상태: 401 Unauthorized - 인증 필요')
elif code == 403:
    print('상태: 403 Forbidden - 접근 권한 없음')
elif code == 404:
    print('상태: 404 Not Found - 리소스 없음')
elif code == 500:
    print('상태: 500 Internal Server Error - 서버 내부 오류')
else:
    print(f'상태: {code} Unknown Status Code')

# 계열 판별
if 200 <= code <= 299:
    print('계열: 2xx - 성공')
elif 400 <= code <= 499:
    print('계열: 4xx - 클라이언트 오류')
elif 500 <= code <= 599:
    print('계열: 5xx - 서버 오류')
