import sys
input = sys.stdin.read
sys.setrecursionlimit(10**7)

# 노드 생성
class Node(object):   
  def __init__(self, data):       
    self.data = data        
    self.left = None
    self.right = None

# 이진 트리 생성
class BinarySearchTree(object):    
  def __init__(self):        
    self.root = None
  
  # 노드 삽입 (반복적 방식)
  def insert(self, data):
    new_node = Node(data)
    if self.root is None:
      self.root = new_node
      return
    current = self.root
    while True:
      if data < current.data:
        if current.left is None:
          current.left = new_node
          break
        current = current.left
      else:
        if current.right is None:
          current.right = new_node
          break
        current = current.right

# 후위 순회(Postorder)
def postorder(node):
  if node is not None:
    postorder(node.left)
    postorder(node.right)
    print(node.data)

# 입력 처리 및 트리 생성
data = input().strip().split()
tree = BinarySearchTree()

# 첫 번째 값을 루트로 삽입
tree.insert(int(data[0]))

# 나머지 값들을 트리에 삽입
for num in data[1:]:
  tree.insert(int(num))

postorder(tree.root)