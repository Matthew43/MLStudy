'''
Created on Apr 29, 2017

@author: 北 纬
'''

import tensorflow as tf
import input_data

# 初始化权重，防止对称性，加入了噪音
def weight_variable(shape):
    return tf.Variable(tf.truncated_normal(shape,stddev=0.1))

# 初始化偏置项bias
def bias_variable(shape):
    return tf.Variable(tf.constant(0.1,shape=shape))

# 卷积层，使用SAME方式
def conv2d(x,W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')

# 采样层
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")


def main():
   
    
    x_data = tf.placeholder(tf.float32, [None,784])
    y_data = tf.placeholder(tf.float32, [None,10])
    
    # 第一层卷积
    W_conv1 = weight_variable([5,5,1,32])
    b_conv1 = bias_variable([32])
    
    x_image = tf.reshape(x_data, shape=[-1,28,28,1])
    
    h_conv1 = tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)
    
    # 第二层卷积
    W_conv2 = weight_variable([5,5,32,64])
    b_conv2 = bias_variable([64])
        
    h_conv2 = tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)
    
    # 全连接层
    W_fc1 = weight_variable([7*7*64,1024])
    b_fc1 = bias_variable([1024])
    
    h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)
    
    # Dropout层
    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
    
    # 输出层
    W_fc2 = weight_variable([1024,10])
    b_fc2 = bias_variable([10])
    
    y = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)
    
    
    
    # 计算损失函数
    loss =   tf.reduce_mean(-tf.reduce_sum(y_data * tf.log(y), reduction_indices=[1]))
    train = tf.train.AdamOptimizer(1e-4).minimize(loss)
    
    # 测试
    correct_prediction = tf.equal(tf.arg_max(y_data, 1), tf.arg_max(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    
    init = tf.initialize_all_variables()
    
    with tf.Session() as sess:
        sess.run(init)
        # 读入数据集
        mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) 
        for i in range(20000):
            # 数据读入
        
            batch_xs, batch_ys = mnist.train.next_batch(50)
            
            sess.run(train, feed_dict={x_data:batch_xs, y_data : batch_ys,keep_prob:0.5})
            
            if i % 500 == 0:
                t_accuracy = sess.run(accuracy, feed_dict={x_data:batch_xs, y_data : batch_ys,keep_prob:0.5})
                print("step ",i," accuracy: ",t_accuracy)

        print('#'*10,"测试",'#'*10)
        print("accuracy:",sess.run(accuracy, feed_dict={x_data:mnist.test.images, y_data:mnist.test.labels,keep_prob:1.0}))
        


if __name__ == '__main__':
    main()