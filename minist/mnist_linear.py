'''
Created on Apr 27, 2017

@author: 北 纬
'''

import tensorflow as tf
import input_data

def main():
   
    
    # 建模
    x_data = tf.placeholder(tf.float32, [None, 784])
       
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x_data, W) + b)
    
    y_data = tf.placeholder(tf.float32, [None, 10])
    loss =   tf.reduce_mean(-tf.reduce_sum(y_data * tf.log(y), reduction_indices=[1]))
    train = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
    
    
    # 测试
    correct_prediction = tf.equal(tf.arg_max(y_data, 1), tf.arg_max(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    # 开始
    init = tf.initialize_all_variables()    
    
    with tf.Session() as sess:
        sess.run(init)
        # 读入数据集
        mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) 
        # 训练
        for i in range(1, 1000):
            # 数据读入
        
            batch_xs, batch_ys = mnist.train.next_batch(100)
            
            sess.run(train, feed_dict={x_data:batch_xs, y_data : batch_ys})
            if i % 10 == 0:
                print("step ", i , 'loss:',sess.run(loss, feed_dict={x_data:batch_xs, y_data : batch_ys}))
  
        
        
        # 测试
        print('#'*10,"测试",'#'*10)
        print("accuracy:",sess.run(accuracy, feed_dict={x_data:mnist.test.images, y_data:mnist.test.labels}))
        

if __name__ == '__main__':
    main()
