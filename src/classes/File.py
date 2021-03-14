"""
Name : File.py
Author : OBR01
Contect : oussama.brich@edissyum.com
Time    : 28/02/2021 20:22
Desc: File Manger class
"""
import csv
import numpy as np
import pandas as pd


class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load_data_from_csv(self):
        """
        :return: N/A
        """
        with open(self.file_path, newline='') as csv_file:
            self.data = list(csv.reader(csv_file, delimiter=","))

    def get_colon_index(self, colon):
        """
        :param colon:
        :return: N/A
        """
        if not self.data:
            print("[Warning] Data not loaded.")
            return None

        for index, colon_name in enumerate(self.data[0]):
            if colon_name == colon: return index
        print("[Warning] Colon not found.")
        return None

    def get_value(self, row, colon):
        """
        :param row:
        :param colon:
        :return: N/A
        """
        colon_index = self.get_colon_index(colon)
        return self.data[row][colon_index]

    def count_line(self):
        """
        :return: number of rows in data
        """
        return len(self.data[1:])

    def adapt_to_training(self):
        """
        :return:
        """
        colon_index = self.get_colon_index('CDMOTDEM')
        for i in range(1, len(self.data)):
            if self.data[i][colon_index] == '':
                self.data[i][colon_index] = 'NoResignation'

    def save_file(self, path):
        """
        :param path:
        :return:
        """
        np.savetxt(path,
                   self.data[1:],
                   delimiter=", ",
                   fmt='% s')

    @staticmethod
    def merge_demission(file1, file2):
        """
        :return:
        """
        print("########################")
        print("#####RUN FUSION DEM#####")
        print("########################")
        client_dem = pd.read_csv(file1, sep=',')
        client_dem_bis = pd.read_csv(file1, sep=',')


        del client_dem['Id']
        del client_dem_bis['Id']
        fusion_dem = pd.DataFrame(client_dem).append(pd.DataFrame(client_dem_bis))

        print(client_dem)
        print(client_dem_bis)
        print(fusion_dem)

        fusion_dem.to_csv('../donnees/fusion/dem.csv', sep=",", index=False)
        print("########################")
        print("#####END FUSION DEM#####")
        print("########################")
