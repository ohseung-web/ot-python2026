# library.py
today = '2025-06-10'

books = {
    "B001": {"title": "파이썬 완전정복", "author": "홍길동",   "genre": "IT",   "total": 3, "available": 3},
    "B002": {"title": "데이터분석 입문", "author": "김데이터", "genre": "IT",   "total": 2, "available": 2},
    "B003": {"title": "알고리즘의 이해", "author": "이알고",   "genre": "IT",   "total": 2, "available": 1},
    "B004": {"title": "채식주의자",      "author": "한강",     "genre": "소설", "total": 4, "available": 4},
    "B005": {"title": "82년생 김지영",   "author": "조남주",   "genre": "소설", "total": 3, "available": 3},
}

loans = {
    "L001": {"member": "박지수", "book_id": "B003", "loan_date": "2025-05-20", "due_date": "2025-06-03", "returned": False},
    "L002": {"member": "최우진", "book_id": "B001", "loan_date": "2025-05-25", "due_date": "2025-06-08", "returned": False},
}

# ─── 1. 도서 목록 조회 ───────────────────────────────────────────
def show_books():
    print("\n도서ID   제목               저자       장르    전체  가능  상태")
    print("-" * 70)
    for bid, b in books.items():
        status = "대출가능" if b["available"] > 0 else "대출불가"
        print(f'{bid:<8} {b["title"]:<18} {b["author"]:<10} {b["genre"]:<6} {b["total"]:<5} {b["available"]:<5} {status}')

# ─── 2. 도서 대출 ────────────────────────────────────────────────
def loan_book():
    member = input("회원명을 입력하세요: ")
    bid    = input("대출할 도서ID를 입력하세요: ")
    if bid not in books:
        print("등록되지 않은 도서입니다.")
        return
    if books[bid]["available"] == 0:
        print("현재 대출 가능한 도서가 없습니다.")
        return
    loan_id  = f"L{len(loans)+1:03d}"
    due_date = '2025-06-24'   # 실습 단순화: 고정값 사용
    loans[loan_id] = {
        "member": member, "book_id": bid,
        "loan_date": today, "due_date": due_date, "returned": False
    }
    books[bid]["available"] -= 1
    print(f"[대출 완료] {member} 님이 '{books[bid]['title']}' 을(를) 대출하였습니다.")
    print(f"대출번호: {loan_id} | 반납예정일: {due_date}")

# ─── 3. 도서 반납 ────────────────────────────────────────────────
def return_book():
    lid = input("대출번호를 입력하세요: ")
    if lid not in loans:
        print("해당 대출 기록이 없습니다.")
        return
    if loans[lid]["returned"]:
        print("이미 반납된 도서입니다.")
        return
    loans[lid]["returned"] = True
    bid = loans[lid]["book_id"]
    books[bid]["available"] += 1
    print(f"[반납 완료] '{books[bid]['title']}' 이(가) 반납되었습니다.")

# ─── 4. 대출 현황 조회 ───────────────────────────────────────────
def show_loans():
    print("\n대출번호  회원명    도서제목           대출일        반납예정일    반납여부")
    print("-" * 78)
    for lid, l in loans.items():
        title   = books[l["book_id"]]["title"]
        status  = "반납완료" if l["returned"] else "대출중"
        print(f'{lid:<9} {l["member"]:<9} {title:<18} {l["loan_date"]:<13} {l["due_date"]:<13} {status}')

# ─── 5. 연체 현황 조회 ───────────────────────────────────────────
def show_overdue():
    print(f"\n=== 연체 현황 (기준일: {today}) ===")
    found = False
    for lid, l in loans.items():
        if not l["returned"] and l["due_date"] < today:
            if not found:
                print("대출번호  회원명    도서제목           반납예정일")
                print("-" * 50)
                found = True
            title = books[l["book_id"]]["title"]
            print(f'{lid:<9} {l["member"]:<9} {title:<18} {l["due_date"]}')
    if not found:
        print("현재 연체된 도서가 없습니다.")

# ─── 6. 장르별 통계 ──────────────────────────────────────────────
def show_genre_stats():
    genre_data = {}
    for bid, b in books.items():
        g = b["genre"]
        if g not in genre_data:
            genre_data[g] = {"total": 0, "loaned": 0}
        genre_data[g]["total"]  += b["total"]
        genre_data[g]["loaned"] += b["total"] - b["available"]
    print("\n장르     전체권수  대출중")
    print("-" * 30)
    for g, d in genre_data.items():
        print(f'{g:<8} {d["total"]:<9} {d["loaned"]}')

# ─── 메인 루프 ───────────────────────────────────────────────────
while True:
    print("\n=== 도서관 대출 관리 시스템 ===")
    print("1. 도서 목록 조회")
    print("2. 도서 대출")
    print("3. 도서 반납")
    print("4. 대출 현황 조회")
    print("5. 연체 현황 조회")
    print("6. 장르별 통계")
    print("0. 종료")
    choice = input("메뉴를 선택하세요: ")
    if   choice == "1": show_books()
    elif choice == "2": loan_book()
    elif choice == "3": return_book()
    elif choice == "4": show_loans()
    elif choice == "5": show_overdue()
    elif choice == "6": show_genre_stats()
    elif choice == "0":
        print("시스템을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")
