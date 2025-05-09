import matplotlib.pyplot as plt
import tensorflow.keras as kr
import tensorflow as tf
import numpy as np

def layers():
    # Content layer where will pull our feature maps
    content_layers = ['block5_conv2'] 

    # Style layers
    style_layers = ['block1_conv1',
                    'block2_conv1',
                    'block3_conv1', 
                    'block4_conv1', 
                    'block5_conv1']
    return content_layers, style_layers


def get_model(styles, contents):
       
    IMAGE_HEIGHT = 300
    IMAGE_WIDTH = 400   
    vgg = kr.applications.vgg19.VGG19(include_top=False, 
                                      weights='imagenet', 
                                      input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3))
    vgg.trainable = False
    
    # Get output layers corresponding to style and content layers 
    style_outputs = [vgg.get_layer(layer_name).output for layer_name in styles]
    content_outputs = [vgg.get_layer(layer_name).output for layer_name in contents]
    model_outputs = style_outputs + content_outputs
   
    return kr.Model(vgg.input, model_outputs)