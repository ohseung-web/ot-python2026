# 게시판 데이터 (리스트 안에 딕셔너리 구조)
# 게시판 데이터 (리스트 안에 딕셔너리 구조)
posts = [
    {'id': 1, 'title': 'Python 기초 질문', 'author': '신입개발자',
     'views': 320, 'comments': ['감사합니다', '저도 몰랐어요', '도움됐어요']},

    {'id': 2, 'title': 'SpringBoot 오류 해결', 'author': '백엔드개발자',
     'views': 850, 'comments': ['해결했습니다!', '저도 같은 문제']},

    {'id': 3, 'title': 'React Vite 설정법', 'author': '프론트개발자',
     'views': 640, 'comments': ['잘됩니다', '완벽해요', '공유감사', '북마크']},

    {'id': 4, 'title': 'MyBatis vs JPA 비교', 'author': '풀스택개발자',
     'views': 1200, 'comments': ['JPA 추천', 'MyBatis도 좋아요']},
]


# -----------------------------------
# 댓글이 가장 많은 게시글 찾기
# -----------------------------------

# 첫 번째 게시글을 기준값으로 설정
top_post = posts[0]
max_comments = len(posts[0]['comments'])

# 게시글을 하나씩 확인
for p in posts:

    # 현재 게시글 댓글 개수
    comment_count = len(p['comments'])

    # 현재 댓글 수가 더 많으면 기준값 변경
    if comment_count > max_comments:
        max_comments = comment_count
        top_post = p


print("댓글이 가장 많은 게시글")
print(top_post['title'], ":", max_comments, "개")


# -----------------------------------
# 조회수 TOP 2 찾기
# -----------------------------------

first_post = None
second_post = None

# 게시글을 하나씩 확인
for p in posts:

    # 첫 번째 값이 없으면 저장
    if first_post == None:
        first_post = p

    # 현재 게시글 조회수가 1위보다 크면
    elif p['views'] > first_post['views']:

        second_post = first_post
        first_post = p

    # 2위 자리 확인
    elif second_post == None or p['views'] > second_post['views']:

        second_post = p


print()
print("=== 조회수 TOP 2 ===")
print("1위 :", first_post['title'], "-", first_post['views'], "회")
print("2위 :", second_post['title'], "-", second_post['views'], "회")


# -----------------------------------
# 전체 댓글 개수 구하기
# -----------------------------------

all_comments = []

# 게시글을 하나씩 확인
for p in posts:

    comments = p['comments']  # 댓글 리스트

    # 댓글을 하나씩 확인
    for c in comments:
        all_comments.append(c)


print()
print("전체 댓글 수 :", len(all_comments), "개")

# # 게시판 데이터
# posts = [
#     {'id': 1, 'title': 'Python 기초 질문', 'author': '신입개발자',
#      'views': 320, 'comments': ['감사합니다', '저도 몰랐어요', '도움됐어요']},
#     {'id': 2, 'title': 'SpringBoot 오류 해결', 'author': '백엔드개발자',
#      'views': 850, 'comments': ['해결했습니다!', '저도 같은 문제']},
#     {'id': 3, 'title': 'React Vite 설정법', 'author': '프론트개발자',
#      'views': 640, 'comments': ['잘됩니다', '완벽해요', '공유감사', '북마크']},
#     {'id': 4, 'title': 'MyBatis vs JPA 비교', 'author': '풀스택개발자',
#      'views': 1200, 'comments': ['JPA 추천', 'MyBatis도 좋아요']},
# ]
 
# # 댓글 수 가장 많은 게시글
# top_comment = max(posts, key=lambda p: len(p['comments']))
# print(f"댓글 최다: '{top_comment['title']}' ({len(top_comment['comments'])}개)")
 
# # 조회수 상위 2개
# sorted_posts = sorted(posts, key=lambda p: p['views'], reverse=True)
# print('\n=== 조회수 TOP 2 ===') 
# for i, p in enumerate(sorted_posts[:2], 1):
#     print(f"  {i}위: [{p['views']}회] {p['title']}")
 
# # 전체 댓글 합치기
# all_comments = []
# for p in posts:
#     all_comments.extend(p['comments'])
# print(f'\n전체 댓글 수: {len(all_comments)}개')
 
