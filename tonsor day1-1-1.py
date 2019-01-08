import tensorflow as tf
###################################################
# 버전 확인
# tf.__version__#버전 확인인데 쉘에서 되나보다 

# 인사 출력 
# 기본 그래프의 노드를 추가하는 것 
# This op is added as a node to the default graph
hello = tf.constant("Hello, TensorFlow!")
# TF 세션 시작 
# start a TF session
sess = tf.Session()
# op를 실행하고 결과값을 얻습니다
# Run the op and get result
print(sess.run(hello))
# b'Hello, TensorFlow!' b는 byte를 의미한다고 한다.
###################################################

