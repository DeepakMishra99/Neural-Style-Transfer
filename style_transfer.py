from model import get_model, layers
from preprocessing import load_image,deprocess_img,img_parser
from losses import compute_grads
import matplotlib.pyplot as plt
import tensorflow.keras as kr
import tensorflow as tf
import numpy as np


def transfer_style(content_img, style_img, epochs=1000): 
    def generate_noisy_image(content_image, noise_ratio):
        """Generates a noisy image by adding random noise to the content image"""
        IMAGE_HEIGHT = 300
        IMAGE_WIDTH = 400
        noise_image = tf.random.uniform([1, IMAGE_HEIGHT, IMAGE_WIDTH, 3], minval=-20, maxval=20)
        input_image = noise_image * noise_ratio + content_image * (1 - noise_ratio)
        return input_image

    # We don't want to train any layers of our model 
    content_layers, style_layers = layers()
    model = get_model(style_layers, content_layers) 
    for layer in model.layers:
        layer.trainable = False
        
    S = load_image(style_img)
    C = load_image(content_img)

    style_outputs = model(S)
    content_outputs = model(C)

    # Get the style and content feature representations (from our specified intermediate layers) 
    _content = [content_layer[0] for content_layer in content_outputs[len(style_layers):]][0]
    _style = [style_layer[0] for style_layer in style_outputs[:len(style_layers)]]
  
    # Set initial image
    G = generate_noisy_image(C, 0.6)
    G = tf.Variable(G, dtype=tf.float32)

    best_loss, best_img = float('inf'), None
  
    # Create a nice config 
    cfg = {
        'model': model,
        'image': G,
        'style_features': _style,
        'content_features': _content
    }
    
    # Create our optimizer
    opt = tf.optimizers.Adam(learning_rate=2.0, beta_1=0.99, epsilon=1e-1)
    
    
   
  
    norm_means = np.array([103.939, 116.779, 123.68])
    min_vals = -norm_means
    max_vals = 255 - norm_means   
  
    for i in range(epochs):
        grads, cost = compute_grads(cfg)
        opt.apply_gradients([(grads, G)])
        clipped = tf.clip_by_value(G, min_vals, max_vals)
        G.assign(clipped)
        
        if cost < best_loss:
            best_loss = cost
            best_img = deprocess_img(G.numpy())

          
      
    return best_img, best_loss 