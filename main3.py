import random
import math


class Node():  # 노드 모양의 데이터형은 없습니다. 클래스 문법을 사용하여 노드 데이터형을 정의합니다.
	def __init__(self):
		self.data = None  # 데이터가 저장되는 부분
		self.link = None  # 링크가 저장되는 부분

def print_nodes(start):  # 연결 리스트의 전체 노드를 출력해줍니다. 매개변수로 시작 노드를 전달 받습니다.
	current = start  # 전달 받은 시작 노드를 현재 노드로 지정해줍니다.
	if current == None:  # 노드에 데이터가 하나도 없는 연결리스트의 경우
		return  # 그냥 반환해줍니다.

	while current.link != start:  # 현재 노드의 링크가 첫번째 노드가 아닐 때까지 반복합니다. ( 현재 노드 링크가 첫번째 노드라면, 원형 연결 리스트에서는 마지막 노드를 의미. ) 즉 전체 노드를 한바퀴 돕니다.
		current = current.link
		x, y = current.data[1:]  # 편의점의 데이터 튜플 속에서 인덱스 1, 2를 가져오면 그게 x,y
		print(f'{current.data[0]} 편의점, 거리: {math.sqrt(x*x + y*y)}')  # 편의점 거리 계산
	print()

def  make_storelist(store):
	global head, current, pre  # 첫번째 노드 / 현재 처리 중인 노드 / current의 바로 앞 노드

	node = Node()  # 빈 노드 생성
	node.data = store

	if head == None:  # 첫 번째 편의점 원형 연결 리스트의 첫번째 노드로 만듦.
		head = node
		node.link = head
		return

	# 첫 번째 편의점 이후부터는 거리를 비교해줘야 합니다.
	# 새 편의점이 첫 번째 편의점보다 가까우면 첫 편의점으로 만듦

	node_x, node_y = node.data[1:]
	node_distance = math.sqrt(node_x*node_x + node_y*node_y)

	head_x, head_y = head.data[1:]
	head_distance = math.sqrt(head_x*head_x + head_y*head_y)

	if head_distance > node_distance:  # 헤드로 지정해둔 곳은 첫 번째 편의점이었습니다. 만약 첫 번째 편의점과의 거리가 더 멀다면 첫 번째 편의점은 뒤로 밀려나야합니다. 그리고 새로 생성된 편의점 노드가 헤드 앞에 오게됩니다.
		node.link = head  # 링크를 첫 번째 편의점으로 지정
		last = head  # 라스트를 헤드로 지정

		while last.link != head:  # 전체를 돕니다.
			last = last.link  # 라스트를 다음 노드로 변경해주면서 반복해주는 것입니다.
		last.link = node  # last.link에 새 노드를 지정해줍니다.
		head = node  # 즉 헤드가 새 노드가 되는 겁니다.
		return

	# 새 편의점 거리가 비교해봤을 때 중간이라면

	current = head		# 현재의 노드에 헤드를 지정합니다.
	while current.link != head:  # 현재 노드가 마지막이 아닐 때까지 반복합니다.
		pre = current  # 이전 노드를 현재 노드로 지정해줍니다.
		current = current.link  # 현재노드가 옆으로 이동합니다.
		current_x, current_y = current.data[1:]
		current_distance = math.sqrt(current_x*current_x + current_y*current_y)
		if current_distance > node_distance:  # 노드 다음에 커런트
			pre.link = node
			node.link = current
			return

	#마지막 편의점!

	current.link = node
	node.link = head


# 전역 변수

head, current, pre = None, None, None

# 메인 코드
if __name__ == "__main__":

	store_array = []
	store_name = 'A'
	for _ in range(10):
		store = (store_name, random.randint(1, 100), random.randint(1, 100))
		store_array.append(store)
		store_name = chr(ord(store_name) + 1)  # 아스키 코드를 이용해 편의점 'A'를 정수로 바꾸어 +1 해주면서 편의점 이름을 ABC 순으로 설정
		# ord(문자)를 이용해서 해당 문자에 해당하는 유니코드 정수로 반환
		# chr(숫자)를 이용해서 숫자에 해당하는 문자를 반환


	for store in store_array:
		make_storelist(store)

	print_nodes(head)