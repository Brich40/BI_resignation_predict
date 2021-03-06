"""
Name : Charts.py
Author : OBR01
Contect : oussama.brich@edissyum.com
Time    : 28/02/2021 20:22
Desc: Charts Manger class
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


class Charts:

    @staticmethod
    def draw_bars(label, data):
        plt.bar(label, data)
        plt.show()

    @staticmethod
    def draw_line_chart(args):
        plt.plot(args['x_data'], args['y_data'])
        plt.title(args['title'])
        plt.xlabel(args['xlabel'])
        plt.ylabel(args['ylabel'])
        plt.xticks(rotation=90)
        plt.show()
