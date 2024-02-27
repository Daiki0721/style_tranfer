import tensorflow as tf

def generate_images(model, input):
  prediction = model(input, training=True)
  return prediction[0]
