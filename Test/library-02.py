# 기준 날짜 (연체 확인용)
today = '2025-06-10'


# 도서 목록
books = [
    {'id':'B001','title':'파이썬 완전정복','author':'홍길동','genre':'IT','total':3,'available':3},
    {'id':'B002','title':'데이터분석 입문','author':'김데이터','genre':'IT','total':2,'available':2},
    {'id':'B003','title':'알고리즘의 이해','author':'이알고','genre':'IT','total':2,'available':1},
    {'id':'B004','title':'채식주의자','author':'한강','genre':'소설','total':4,'available':4},
    {'id':'B005','title':'82년생 김지영','author':'조남주','genre':'소설','total':3,'available':3},
]


# 대출 기록
loans = [
    {'loan_id':'L001','member':'박지수','book_id':'B003','loan_date':'2025-05-20','due_date':'2025-06-03','returned':False},
    {'loan_id':'L002','member':'최우진','book_id':'B001','loan_date':'2025-05-25','due_date':'2025-06-08','returned':False},
]


# 1️⃣ 도서 목록 조회
def show_books():

    print("\n도서ID   제목          저자      장르    전체  가능")

    for book in books:

        print(book['id'], book['title'], book['author'],
              book['genre'], book['total'], book['available'])



# 2️⃣ 도서 대출
def loan_book():

    member = input("회원명 입력: ")
    book_id = input("도서ID 입력: ")

    # 도서 찾기
    for book in books:

        if book['id'] == book_id:

            # 대출 가능한지 확인
            if book['available'] == 0:
                print("대출 가능한 도서가 없습니다")
                return

            # 대출번호 생성
            loan_id = "L00" + str(len(loans)+1)

            # 반납 예정일 (실습 단순화)
            due_date = "2025-06-24"

            # 대출 기록 추가
            loans.append({
                'loan_id':loan_id,
                'member':member,
                'book_id':book_id,
                'loan_date':today,
                'due_date':due_date,
                'returned':False
            })

            # 대출 가능 수량 감소
            book['available'] -= 1

            print("대출 완료 :", book['title'])

            return

    print("등록되지 않은 도서입니다")



# 3️⃣ 도서 반납
def return_book():

    loan_id = input("대출번호 입력: ")

    for loan in loans:

        if loan['loan_id'] == loan_id:

            if loan['returned'] == True:
                print("이미 반납된 도서입니다")
                return

            loan['returned'] = True

            # 도서 수량 증가
            for book in books:
                if book['id'] == loan['book_id']:
                    book['available'] += 1

            print("반납 완료")
            return

    print("대출 기록이 없습니다")



# 4️⃣ 대출 현황 조회
def show_loans():

    print("\n대출번호 회원명 도서ID 대출일 반납예정일 상태")

    for loan in loans:

        status = "반납완료"

        if loan['returned'] == False:
            status = "대출중"

        print(loan['loan_id'], loan['member'], loan['book_id'],
              loan['loan_date'], loan['due_date'], status)



# 5️⃣ 연체 현황
def show_overdue():

    print("\n연체 도서")

    found = False

    for loan in loans:

        if loan['returned'] == False and loan['due_date'] < today:

            print(loan['loan_id'], loan['member'], loan['due_date'])

            found = True

    if found == False:
        print("연체 없음")



# 6️⃣ 장르별 통계
def show_genre_stats():

    genre_data = {}

    for book in books:

        genre = book['genre']

        if genre not in genre_data:
            genre_data[genre] = 0

        genre_data[genre] += book['total']

    print("\n장르별 도서 수")

    for g in genre_data:
        print(g, genre_data[g])



# 메인 메뉴
while True:

    print("\n=== 도서관 시스템 ===")
    print("1 도서목록")
    print("2 도서대출")
    print("3 도서반납")
    print("4 대출현황")
    print("5 연체조회")
    print("6 장르통계")
    print("0 종료")

    menu = input("선택: ")

    if menu == "1":
        show_books()

    elif menu == "2":
        loan_book()

    elif menu == "3":
        return_book()

    elif menu == "4":
        show_loans()

    elif menu == "5":
        show_overdue()

    elif menu == "6":
        show_genre_stats()

    elif menu == "0":
        break