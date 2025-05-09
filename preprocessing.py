
import tensorflow.keras as kr
import tensorflow as tf
import numpy as np

import warnings
warnings.filterwarnings('ignore')



def img_parser(filename):
    img_string = tf.io.read_file(filename)
    img = tf.image.decode_jpeg(img_string, channels=3)
    img = tf.cast(img, dtype=tf.float32)

    
    # Resize the image
    IMAGE_HEIGHT = 300
    IMAGE_WIDTH = 400
    img = tf.image.resize(img, size=(IMAGE_HEIGHT, IMAGE_WIDTH))
    img = tf.expand_dims(img, axis=0)   # Add batch dimension
    return img

def load_image(filename):
    img = img_parser(filename)
    img = kr.applications.vgg19.preprocess_input(img)
    return img

def deprocess_img(processed_img):
    x = processed_img.copy()
    if len(x.shape) == 4:
        x = np.squeeze(x, 0)
    assert len(x.shape) == 3, ("Input to deprocess image must be an image of "
                             "dimension [1, height, width, channel] or [height, width, channel]")
    if len(x.shape) != 3:
        raise ValueError("Invalid input to deprocessing image")
  
    # perform the inverse of the preprocessing step
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    x = x[:, :, ::-1]  # Convert back to RGB from BGR

    x = np.clip(x, 0, 255).astype('uint8')
    return x