"""
Name : Charts.py
Author : OBR01
Contect : oussama.brich@edissyum.com
Time    : 28/02/2021 20:22
Desc: Charts Manger class
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import src.classes.File


class Stats:

    @staticmethod
    def count_value(count_args, data_file):
        """
        :param count_args:
        :param data_file:
        :return:
        """
        count_equal = 0
        count_not_equal = 0
        for i in range(data_file.count_line()):
            if data_file.get_value(i, count_args['colon']) == count_args['value']:
                count_equal += 1
            else:
                count_not_equal += 1

        return {
            count_args['labels']['count_equal']: count_equal,
            count_args['labels']['count_not_equal']: count_not_equal
        }

    @staticmethod
    def count_by_year(count_args, data_file):
        """
        :param count_args:
        :param data_file:
        :return:
        """
        years = {}
        for i in range(1, data_file.count_line()):
            date_value = data_file.get_value(i, count_args['colon'])
            if date_value != count_args['value']:
                year = date_value[:4]

                # If year not already detected
                if year not in years:
                    years[date_value[:4]] = 1
                else:
                    years[date_value[:4]] += 1

        return years
