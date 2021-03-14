"""
Name : Charts.py
Author : OBR01
Contect : oussama.brich@edissyum.com
Time    : 28/02/2021 20:22
Desc: Charts Manger class
"""
import matplotlib.pyplot as plt


class Charts:

    @staticmethod
    def draw_bars(label, data):
        """
        :param label:
        :param data:
        :return: N/A
        """
        plt.bar(label, data)
        plt.show()

    @staticmethod
    def draw_line_chart(args):
        """
        :param args:
        :return: N/A
        """
        plt.plot(args['x_data'], args['y_data'])
        plt.title(args['title'])
        plt.xlabel(args['xlabel'])
        plt.ylabel(args['ylabel'])
        plt.xticks(rotation=90)
        plt.show()
