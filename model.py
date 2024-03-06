import tensorflow as tf
from matplotlib import pyplot as plt
from IPython import display

input = "/Users/daiki/Desktop/style_transfer/style_transfer/media/img/Cartoons_00007_01.jpg"
def load(image_file):
  # Read and decode an image file to a uint8 tensor
  image = tf.io.read_file(image_file)
  image = tf.io.decode_jpeg(image)

  # Convert both images to float32 tensors
  input_image = tf.cast(image, tf.float32)

  return input_image

inp = load(input)
# Casting to int for matplotlib to display the images
inp = tf.image.resize(inp, [256,256])
inp = tf.expand_dims(inp, 0)

print(inp.shape)



generator = tf.keras.models.load_model('my_model.h5',compile=False)

def generate_images(model, input):
  prediction = model(input, training=True)
  return prediction[0]


pred = generate_images(generator, inp)
print(pred)

plt.imshow(pred)
plt.axis('off')
plt.show()
