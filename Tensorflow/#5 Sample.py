import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(500).astype(np.float16)
y_data = 300  * x_data + 10  # y = 300x + 10

### create tensorflow structure start ###
a = tf.Variable(tf.random_uniform([1], -1000, 1000))
b = tf.Variable(tf.zeros([1]))
y = a*x_data + b

loss = tf.reduce_mean(tf.square(y-y_data)) # (y-y_data)^2
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
### create tensorflow structure end ###

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(a), sess.run(b))

