# 큐가 꽉 찼는가?
def is_queue_full() :
	global SIZE, queue, front, rear
	if (rear == SIZE-1) :
		return True
	else :
		return False

# 큐가 비었는지 체크
def is_queue_empty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

# 큐에 데이터를 삽입
def en_queue(data) :
	global SIZE, queue, front, rear
	if (is_queue_full()) :
		print("큐가 꽉 찼습니다.")
		return
	rear += 1
	queue[rear] = data

# 큐에서 데이터를 추출
def de_queue() :
	global SIZE, queue, front, rear
	if (is_queue_empty()) :
		print("큐가 비었습니다.")
		return None
	front += 1
	data = queue[front]
	queue[front] = None


# 맨 앞쪽 손님들부터 식당에 들어갈 수 있도록
# 한칸씩 앞으로 당겨주는 과정입니다.
	for i in range(front + 1, rear + 1):
		queue[i - 1] = queue[i]
		queue[i] = None

	front = -1
	rear -= 1
#뒤로 다시 당김

	return data

# front+1 위치의 데이터 확인.
def peek() :
	global SIZE, queue, front, rear
	if (is_queue_empty()) :
		print("큐가 비었습니다.")
		return None
	return queue[front+1]

# 전역 변수
SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear = -1

# 메인 코드
if __name__ == "__main__" :
	en_queue('정국')
	en_queue('뷔')
	en_queue('지민')
	en_queue('진')
	en_queue('슈가')
	print("대기 줄 상태 : ", queue)

	for _ in range(rear+1) :
		print(de_queue(), '님 식당에 들어감')
		print("대기 줄 상태 : ", queue)

	print("식당 영업 종료!")
