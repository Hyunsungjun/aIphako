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
# 이어지네..? 그냥 여기서 쭉 이어가도록 하겠습니다.
###################################################
# Placeholder
# 특별한 노드이다 필요한 그래프를 만들어 놨다면 가져와서 사용하는 것 

a = tf.placeholder(tf.float32) #플레이스 노드를 만들고 애더 노드를 만든다.
b = tf.placeholder(tf.float32)
adder_node = a + b # + provides a shorcut for tf.add(a, b) 숏컷 제공 

print(sess.run(adder_node, feed_dict = {a: 3,b: 4.5})) #feed dict가 place holer에 할당이 된다 
print(sess.run(adder_node, feed_dict = {a: [1,3], b: [2,4]}))
# 결과값 
# 7.5
# [3. 7.]
###################################################
# 1. Build graph using TensorFlow operations
# 2. feed data and run graph sess.run(op,feed_dict={x:x_data})
# 3. update variables in the graph(and retrun values)

# Tensor Rankes, Shapes, and Types 
# Rank 
# t = [[1,2,3],[4,5,6],[7,8,9]]
# Rank    Math entity     Python example
# 0   Scalar(magnitude only) s = 1
# 1   Vector(magnitude and direction) v=[1.1,2.2,3.3]
# 2   Matrix(table of numbers) m=[[1,2,3],[4,5,6],[7,8,9]]
# 3   3-Tensor(cube of numbers) t=[[[2],[4],[6]], [[8],[10],[12]], [[14],[16],[18]]]
# 4   n-Tensor(you get the idea)

# Shapes
# t = [[1,2,3],[4,5,6],[7,8,9]]  (3,3) [3,3] 이렇게 t를 나타냄
# Rank    Shape   Dimension number    Example
# 0   []              0-D  A 0-D Tensor. A scalar
# 1   [D0]            1-D  A 1-D tensor with shape[5]
# 2   [D0,D1]         2-D  A 2-D Tensor with shape[3,4]
# 3   [D0,D1,D2]      3-D  A 3-D Tensor with shape[1,4,3]
# n   [D0,D1,...Dn-1] n-D  A tensor wiht shape [D0,D1,...Dn-1]

# Types 
# t = [[1,2,3],[4,5,6],[7,8,9]]
# Data type   Python type     Description
# DT_FLOAT    tf.float32      32 bits floating point
# DT_DOUBLE   tf.float64      64 bits floating point
# DT_INT8     tf.int8         8 bits ingned integer
# DT_INT16    tf.int16        16 bits signed integer
# DT_INT32    tf.int32        32 bits signed integer
# DT_INT64    tf.int64        64 bits signed integer

# 마지막 정리 
# 1. 그래프 설계 
# 2. 그래프 그림 
# 3. 그래프로 업데이트 