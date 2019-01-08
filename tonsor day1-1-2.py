import tensorflow as tf
###################################################
node1 = tf.constant(3.0, tf.float32)#float32 델타 타입? 검색해볼것 
node2 = tf.constant(4.0) # also tf.float32 implicitly 암시적으로 , 노드 추가
node3 = tf.add(node1, node2) # 더하기 노드를 만든다 add함수를 썻지만 3 = 1 + 2를 해도무방하다 

print("node1:", node1, "node2:", node2)
print("node3:", node3)
# 결과값이라고 보기는 힘들고 텐서라고 말해주는 것 
# node1: Tensor("Const:0", shape=(), dtype=float32) 
# node2: Tensor("Const_1:0", shape=(), dtype=float32)
# node3: Tensor("Add:0", shape=(), dtype=float32)

sess = tf.Session()
print("sess.run(node1, node2): ", sess.run([node1, node2]))
print("sess.run(node3): ", sess.run(node3))
# 결과값
# sess.run(node1, node2):  [3.0, 4.0]
# sess.run(node3):  7.0
# 사실상 3이랑 4를 더한것 고정 값을 줬으니 당연한 것 
###################################################
# 1.Build graph using TenssorFlow operations
# 2.feed data and run graph (operation) sess.run(op)
# 3.update variables in the graph


# 1.텐서플로우를 사용하여 그래프를 작성 
# 2.데이터를 받고 그래프를 실행한다 sess.run으로 작동
# 3.그래프에서 여러값을 업데이트 한다