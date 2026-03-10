phone_book = { }
phone_book["홍길동"] = "010-1234-5678"

print(phone_book)
phone_book = {"홍길동": "010-1234-5678"}
phone_book["강감찬"] = "010-1234-5679"
phone_book["이순신"] = "010-1234-5680"
print(phone_book['이순신'])

print(phone_book.keys())

dict = {'Name': '홍길동', 'Age': 7, 'Class': '초급'}
print (dict['Name'])
print (dict['Age'])

for key in sorted(phone_book.keys()):
     print(key, phone_book[key])

for key in (phone_book.keys()):
     print(key, phone_book[key])

