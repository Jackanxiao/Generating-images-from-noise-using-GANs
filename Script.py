
#Build a generative adversarial network (GAN) to generate digit images from a noise distribution with TensorFlow.

from __future__ import division, print_function, absolute_import

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf



# Import MNIST data# Impor
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

