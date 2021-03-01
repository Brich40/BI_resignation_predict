"""
Name : main.py
Author : OBR01
Contect : oussama.brich@edissyum.com
Time    : 01/03/2021 21:21
Desc: main file
"""

from src.classes.File import File

# Global vars
CSV_FILE_PATH = "../donnees/data_mining_DB_clients_tbl.csv"


def main():
    file = File(CSV_FILE_PATH)
    file.load_data_from_csv()
    print(file.data[0])
    print(file.get_colon_index('CDSEXE'))
    return 0


if __name__ == "__main__":
    main()
