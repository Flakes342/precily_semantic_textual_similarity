import numpy as np                 # linear algebra
import pandas as pd                # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf            # tensorflow for ML models
import tensorflow_hub as hub       # contains USE4
from numpy import dot              # to calculate the dot product of two vectors
from numpy.linalg import norm      # for finding the norm of a vector



class MachineLearningCode:
  def __init__ (self):
    self.text1 = None
    self.text2 = None
    
  def embed(self, input):
    module_import = "https://tfhub.dev/google/universal-sentence-encoder/4" #Encoder is imported from this URL
    encoder = hub.load(module_import)   # initialising an embed function which returns the encoded text
    return encoder(input)

  def predict (self, text1, text2):
    messages = [text1, text2]
    message_embeddings = self.embed(messages)
    t = tf.make_ndarray(tf.make_tensor_proto(message_embeddings))
    cos_sim = dot(t[0], t[1])/(norm(t[0])*norm(t[1]))
    y = (cos_sim+1)/2
    return y
