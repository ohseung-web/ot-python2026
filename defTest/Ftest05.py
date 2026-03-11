def greet(name, msg="별일 없죠?"):
   print("안녕 ", name + ', ' + msg)

greet("영희")

def add(a, b):   
    result = a + b
    return result

print("합계:", add(10,20))
print("합계:", add(3,5))