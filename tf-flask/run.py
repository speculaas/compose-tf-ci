'''
hello world example using tensorflow.

'''
import tensorflow as tf


from flask import Flask
from redis import Redis

hello_ = tf.constant('Hello, xTensorFlow!')
sess = tf.Session() 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'inside flask:{} .\n'.format(sess.run(hello_))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

sess.close()

