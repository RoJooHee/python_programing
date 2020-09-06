import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 하나만 출력합니다
print("# 하나만 출력합니다.")
print("Hello Python Programming...!")
print()

# 여러개를 출력합니다.
print("# 여러개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "송윤석입니다!")

print('"안녕하세요"라고 말했습니다.')
print("\"안녕하세요\"라고 말했습니다.")

print("'배가 고픕니다'라고 생각했습니다")
print('\'배가 고픕니다\'라고 생각했습니다.')

print("\\ \\ \\ \\")

print("안녕"+"하세요")
print("안녕하세요"+"!")

print("안녕하세요"*3)
print(3*"안녕하세요")

print("안녕"+"하세요"*3)
print(("안녕"+"하세요")*3)
print("안녕"+("하세요"*3))

print("# 기본적인 연산")
print(15, "+", 4, "=", 15+4)
print(15, "-", 4, "=", 15-4)
print(15, "*", 4, "=", 15*4)
print(15, "/", 4, "=", 15/4)
