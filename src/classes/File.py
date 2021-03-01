"""
Name : File.py
Author : OBR01
Contect : oussama.brich@edissyum.com
Time    : 28/02/2021 20:22
Desc: File Manger class
"""
import csv


class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load_data_from_csv(self):
        with open(self.file_path, newline='') as csv_file:
            self.data = list(csv.reader(csv_file, delimiter=","))

    def get_colon_index(self, colon):
        if not self.data:
            print("[Warning] Data not loaded.")
            return None

        for index, colon_name in enumerate(self.data[0]):
            if colon_name == colon: return index
        print("[Warning] Colon not found.")
        return None

