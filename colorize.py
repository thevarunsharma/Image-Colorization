import numpy as np
from scipy.misc import imresize, imread, imsave
#import tensorflow.compat.v1 as tf
#tf.disable_v2_behavior()
from tensorflow.keras.models import load_model

model = load_model('./utils/unet.hdf5')
#graph = tf.get_default_graph()

def get_colored(gray_path='./static/gray.jpg', color_path='./static/color.jpg'):
    gray = imresize(imread(gray_path), (32,32))
    if gray.shape[2]>=3: gray = gray.mean(axis=-1)
    gray = gray/255
    #with graph.as_default():
    color = model.predict(gray.reshape((1,32,32,1)))[0]
    imsave(color_path, imresize(color, (200,200)))
    imsave(gray_path, imresize(gray, (200,200)))
