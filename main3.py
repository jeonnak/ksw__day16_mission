class Node():  # 노드 모양의 데이터형은 없습니다. 클래스 문법을 사용하여 노드 데이터형을 정의합니다.
	def __init__(self):
		self.data = None  # 데이터가 저장되는 부분
		self.llink = None  # 왼쪽 링크가 저장되는 부분
		self.rlink = None  # 오른쪽 링크가 저장되는 부분

def print_nodes(start):  # 연결 리스트의 전체 노드를 출력해줍니다. 매개변수로 시작 노드를 전달 받습니다.
	current = start  # 전달 받은 시작 노드를 현재 노드로 지정해줍니다.
	if current.rlink == None:
		return  # 반환해줍니다.
	print("정방향 --> ", end=' ')  # 정방향 출력
	print(current.data, end=' ')
	while current.rlink != None:
		current = current.rlink
		print(current.data, end=' ')
	print()
	print("역방향 --> ", end=' ')  # 역방향 출력
	print(current.data, end=' ')

	while current.llink != None:
		current = current.llink
		print(current.data, end=' ')

# 전역 변수

head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]

# 메인 코드
if __name__ == "__main__":

	node = Node()
	node.data = data_array[0]
	head = node

	for data in data_array[1:]:
		pre = node
		node = Node()
		node.data = data
		pre.rlink = node
		node.llink = pre

	print_nodes(head)