# 큐가 꽉 찼는가?
def is_queue_full():
	global SIZE, queue, front, rear
	if (rear + 1) % SIZE == front:
		return True
	else:
		return False

# 큐가 비었는지 체크
def is_queue_empty():
	global SIZE, queue, front, rear
	if front == rear:
		return True
	else:
		return False

# 큐에 데이터를 삽입
def en_queue(data):
	global SIZE, queue, front, rear
	if is_queue_full():
		print("큐가 꽉 찼습니다.")
		return
	rear = (rear + 1) % SIZE
	queue[rear] = data

# 큐에서 데이터를 추출
def de_queue():
	global SIZE, queue, front, rear
	if is_queue_empty():
		print("큐가 비었습니다.")
		return None
	front = (front + 1) % SIZE
	data = queue[front]
	queue[front] = None
	return data

# (front+1)%SIZE 위치의 데이터 확인.
def peek():
	global SIZE, queue, front, rear
	if is_queue_empty():
		print("큐가 비었습니다.")
		return None
	return queue[(front + 1) % SIZE]

def call_waiting() :
	global SIZE, queue, front, rear

	time = 0

	for i in range((front+1)% SIZE, (rear+1)%SIZE):
		time += queue[i][1]  # 대기시간을 총합해줍니다.

	return time

# 전역 변수
SIZE = 6
queue = [ None for _ in range(SIZE) ]
front = rear = 0

# 메인 코드
if __name__ == "__main__" :
	call_status = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]

	for call in call_status :
		print("귀하의 대기 예상시간은 ", call_waiting(), "분입니다.")
		print("현재 대기 콜 --> ", queue)
		en_queue(call)
		print()

	print("최종 대기 콜 --> ", queue)
	print("프로그램 종료!")