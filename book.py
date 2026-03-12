# [오후] 도서 대여 및 재고 관리 시스템
books = {"파이썬 기초": 3, "자바의 정석": 1, "스프링 부트 실무": 0}

def show_inventory():
    print("\n--- [현재 도서 재고 목록] ---")
    print(f"{'도서명':<15} | {'재고':>5}")
    print("-" * 25)
    for name, stock in books.items():
        status = "대여가능" if stock > 0 else "품절"
        print(f"{name:<15} | {stock:>2} ({status})")

def rent_book(name):
    if name in books:
        if books[name] > 0:
            books[name] -= 1
            print(f"✅ '{name}' 대여가 완료되었습니다.")
        else:
            print(f"❌ '{name}'은 재고가 없습니다.")
    else:
        print("❓ 존재하지 않는 도서명입니다.")

def calculate_penalty(days):
    if days <= 7:
        return days * 500
    return (7 * 500) + ((days - 7) * 1000)

def main():
    while True:
        print("\n--- 도서 대여 관리 시스템 ---")
        print("1. 도서 목록 보기\n2. 도서 대여하기\n3. 연체료 확인\n4. 프로그램 종료")
        choice = input("원하는 메뉴 번호를 선택하세요: ")

        if choice == '1':
            show_inventory()
        elif choice == '2':
            book_name = input("대여할 도서명을 입력하세요: ")
            rent_book(book_name)
        elif choice == '3':
            try:
                days = int(input("연체 일수를 입력하세요: "))
                print(f"⚠️ 총 연체료는 {calculate_penalty(days):,d}원 입니다.")
            except ValueError:
                print("숫자만 입력 가능합니다.")
        elif choice == '4':
            print("프로그램을 종료합니다. 수고하셨습니다!")
            break
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()