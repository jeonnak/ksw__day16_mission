import random

## 함수 선언 부분 ##
def is_stackfull():  # 스택이 꽉 찼는지 여부
	global SIZE, stack, top
	if top >= SIZE-1:
		return True
	else :
		return False

def push(data):  # 스택에 데이터를 삽입
	global SIZE, stack, top
	if is_stackfull():
		print("스택이 꽉 찼습니다.")
		return
	top += 1
	stack[top] = data

def is_stackempty():  # 스택이 비었는지 확인
	global SIZE, stack, top
	if top == -1:
		return True
	else :
		return False

def pop():  # 스택에서 데이터를 추출
	global SIZE, stack, top
	if is_stackempty():
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

def peek() :  # 데이터 확인
	global SIZE, stack, top
	if is_stackempty():
		return None
	return stack[top]

# 전역 변수
SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1

# 메인 코드
if __name__ == "__main__":

	color_array = ["빨강", "파랑", "초록", "노랑", "보라", "주황"]
	random.shuffle(color_array)

	print("과자집에 가는길 : ", end=' ')
	for color in color_array:
		push(color)
		print(color, "-->", end=' ')
	print("과자집")

	print("우리집에 오는길 : ", end=' ')
	while True:
		color = pop()
		if color == None:
			break
		print(color, "-->", end=' ')
	print("우리집")