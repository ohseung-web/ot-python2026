def total_price(book_list):
    total = 0
    print("--- 도서 목록 ---")
    for name, price in book_list: # 튜플 언패킹 사용
        print(f"도서명: {name}, 가격: {price}원")
        total += price
    return total

books = [
    ("파이썬 기초", 15000), 
    ("자바의 정석", 25000), 
    ("React 입문", 18000)
    ]
result = total_price(books)
print(f"\n전체 도서 합계: {result}원")