import tensorflow as tf
import numpy as np
import os
from PIL import Image as Pil_image
model = tf.keras.models.load_model('Lexa_pidor1.h5')
labels_inv = {'Cargo': 0,
              'Military': 1,
              'Carrier': 2,
              'Cruise': 3,
              'Tankers': 4}
labels = {v:k for k,v in labels_inv.items()}
def predict(path):
  img_shape = 128
  img = tf.keras.preprocessing.image.load_img(path, target_size=(img_shape,img_shape), interpolation='lanczos')
  img = tf.keras.preprocessing.image.img_to_array(img)
  img = img / 255
  pred = model.predict(np.array([img]))
  pred_label = np.argsort(pred)
  for i in pred_label[0][-1:-3:-1]:
    if float(f'{pred[0][i]*100:0.2f}') > 75:
      print(f"{labels[i]} Ship : {pred[0][i]*100:0.2f} %")
      print()
      return 
    else:
      print('not ship')