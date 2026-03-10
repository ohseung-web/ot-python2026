# API 응답 데이터 (딕셔너리)
response = {
    'code': 200,
    'message': 'success',
    'data': [
        {'userId': 'user01', 'name': '이자바', 'score': 95},
        {'userId': 'user02', 'name': '박리액트', 'score': 82},
        {'userId': 'user03', 'name': '최스프링', 'score': 91},
        {'userId': 'user04', 'name': '정마이바티스', 'score': 78},
    ]
}

# 응답 코드가 200이면 정상 처리
if response['code'] == 200:

    print('=== 전체 성적 ===')

    # 학생 정보 리스트 가져오기
    students = response['data']

    # 리스트에 있는 학생 정보를 하나씩 확인
    for student in students:

        # 딕셔너리에서 데이터 꺼내기
        name = student['name']
        userid = student['userId']
        score = student['score']

        # 학생 성적 출력
        print(f"{name} ({userid}): {score}점")


    # -----------------------------
    # 90점 이상 학생 찾기
    # -----------------------------

    # 우수 학생을 저장할 리스트
    top_students = []

    # 다시 학생 리스트 확인
    for student in students:

        # 점수가 90점 이상이면
        if student['score'] >= 90:

            # 우수 학생 리스트에 추가
            top_students.append(student)

    print(f'\n=== 우수 수강생 (90점 이상): {len(top_students)}명 ===')

    # 우수 학생 출력
    for student in top_students:
        print(f"★ {student['name']}: {student['score']}점")


# 응답 코드가 200이 아닐 경우
else:
    print(f"오류 발생: {response['message']}")


# # API 응답 시뮬레이션
# response = {
#     'code'   : 200,
#     'message': 'success',
#     'data'   : [
#         {'userId': 'user01', 'name': '이자바', 'score': 95},
#         {'userId': 'user02', 'name': '박리액트', 'score': 82},
#         {'userId': 'user03', 'name': '최스프링', 'score': 91},
#         {'userId': 'user04', 'name': '정마이바티스', 'score': 78},
#     ]
# }
 
# if response['code'] == 200:
#     print('=== 전체 성적 ===') 
#     for item in response['data']:
#         print(f"  {item['name']} ({item['userId']}): {item['score']}점")
 
#     # 90점 이상 필터링
#     top = [d for d in response['data'] if d['score'] >= 90]
#     print(f'\n=== 우수 수강생 (90점 이상): {len(top)}명 ===') 
#     for item in top:
#         print(f"  ★ {item['name']}: {item['score']}점")
# else:
#     print(f"오류 발생: {response['message']}")
 
