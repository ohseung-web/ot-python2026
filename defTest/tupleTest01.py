a = [1, 2, 3] # 리스트
b = (1, 2, 3) # 튜플

a[0] = 10
# b[0] = 10
print(a)
print(b)

fruit = ("apple", "banana", "orange")

print(fruit[0])
print(fruit[1])

days = ("월", "화", "수", "목", "금", "토", "일")
print(days)

t = 1, 2, 3
print(t)

c, d = (10, 20)
print(c)
print(d)

student = ("김철수", 20, "컴퓨터공학")
print("이름:", student[0])
print("나이:", student[1])
print("학과:", student[2])

scores = (80, 90, 75, 100)
tot =0
avg = 0
for s in scores:
   tot += s
avg = tot / len(scores)
print(f"합계:{tot}")   
print(f"평균:{avg:.1f}")   
