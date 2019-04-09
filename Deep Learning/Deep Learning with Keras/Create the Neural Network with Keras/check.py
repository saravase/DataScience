# Import Libraries
import tensorflow as tf

# Print version
print("Tensrflow version is :" +str(tf.__version__))

# Verify session works
hello = tf.constant('Hello optimus this is tensorflow')
sess = tf.Session()
print(sess.run(hello))