import tensorflow as tf

def generate_images(model, input):
  prediction = model(input, training=True)
  return prediction[0]

data = form.cleaned_data
print(data)
obj = UploadImage(**data)
print(obj)
