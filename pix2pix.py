import tensorflow as tf
from matplotlib import pyplot as plt
from IPython import display


def load(image_file):
  # Read and decode an image file to a uint8 tensor
  image = tf.io.read_file(image_file)
  image = tf.io.decode_jpeg(image)
  # Convert both images to float32 tensors
  inp = tf.cast(image, tf.float32)
  inp = tf.image.resize(inp, [256,256])
  inp = tf.expand_dims(inp, 0)
  return inp

def generate_images(model, input):
  prediction = model(input, training=True)
  return prediction[0]
