heroes = []
heroes.append("아이언맨")
['아이언맨']
heroes.append("닥터 스트레인지")
print(heroes)
['아이언맨', '닥터 스트레인지']

letters = ['A', 'B', 'C', 'D', 'E', 'F']

print(letters[0])
print(letters[1])
print(letters[2])
print(letters[0:3])

# 리스트에서 항목 변경하기
heroes = [ "아이언맨", "토르", "헐크", "스칼렛 위치" ]
# heroes[1] = "닥터 스트레인지"
# print(heroes)

# heroes.remove("스칼렛 위치")
# print(heroes)

# if "헐크" in heroes:
#   heroes.remove("헐크")
# print(heroes)

# pop()으로 삭제하기
# heroes.pop()
# print(heroes)

# for hero in heroes:
#   print(hero,end=" ")
heroes.sort()
print(heroes)