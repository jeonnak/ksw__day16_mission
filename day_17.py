import random

class Tree_node() :
	def __init__ (self):
		self.left = None
		self.data = None
		self.right = None

memory = []
root = None

# 편의점 물품
data_ary = ['바나나 맛 우유', '레쓰비 캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라' , '삼각김밥']
# 20개 중복o
sell_ary = [random.choice(data_ary) for _ in range(20)]

print('오늘 판매된 물건(중복O) -->', sell_ary)

node = Tree_node()
node.data = sell_ary[0]
root = node
memory.append(node)

# 이진 탐색 트리

for name in sell_ary[1:]:

	node = Tree_node()
	node.data = name

	current = root
	while True :
		if name == current.data:
			break
		if name < current.data:
			if current.left == None:
				current.left = node

                #  판매되지 않은 물품이 자리함
				memory.append(node)
				break
			current = current.left
		else :
			if current.right == None:
				current.right = node
                #  판매되지 않은 물품이 자리함
				memory.append(node)
				break
			current = current.right

print("이진 탐색 트리 구성 완료!")

def order(node):
	if node == None:
		return
	print(node.data, end = ' ')
	order(node.left)
	order(node.right)

print('오늘 판매된 종류(중복X)--> ', end = ' ')
order(root)