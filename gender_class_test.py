# coding=utf8

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from models.gender_model import CNN
from data.mtfl_data import read_data_sets, BatchRenderer

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_float('lr', 1e-2, 'learning rate')
tf.app.flags.DEFINE_float('valid', 0.2, 'fraction of validation set')
tf.app.flags.DEFINE_integer('n_epoch', 1000, 'number of epochs')
tf.app.flags.DEFINE_integer('batch_size', 128, 'batch size')
tf.app.flags.DEFINE_string('train_dir', 'gender_model', 'dir to store models')

# Global settings
szImg = 39
n_x = szImg * szImg
n_y = 2

def main(args=None):
    nn = CNN(
        input_shape=[FLAGS.batch_size, szImg, szImg, 1],
        n_filter=[20, 40, 60, 80],
        n_hidden=[120],
        n_y=n_y,
        receptive_field=[[4, 4], [3, 3], [3, 3], [2, 2]],
        pool_size=[[2, 2], [2, 2], [2, 2], [1, 1]])

    nn.test()

if __name__ == '__main__':
    tf.app.run()
