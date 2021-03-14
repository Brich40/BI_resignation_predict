"""
Name : AI.py
Author : OBR01
Contect : oussama.brich@edissyum.com
Time    : 07/03/2021 01:06
Desc:
"""
import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing


class AI:
    def __init__(self, file, colons):
        self.file = file
        self.colons = colons

    def train(self, predict_colon):
        abalone_train = pd.read_csv(
            self.file,
            names=self.colons)
        print(abalone_train.head())

        abalone_features = abalone_train.copy()
        abalone_labels = abalone_features.pop(predict_colon)
        abalone_features = np.array(abalone_features)
        print(abalone_features)

        abalone_model = tf.keras.Sequential([
            layers.Dense(64),
            layers.Dense(1)
        ])
        abalone_model.compile(loss=tf.losses.MeanSquaredError(),
                              optimizer=tf.optimizers.Adam())

        abalone_model.fit(abalone_features, abalone_labels, epochs=10)
