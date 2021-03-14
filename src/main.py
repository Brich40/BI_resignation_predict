"""
Name : main.py
Author : OBR01
Contect : oussama.brich@edissyum.com
Time    : 01/03/2021 21:21
Desc: main file
"""

from src.classes.File import File
from src.classes.Stats import Stats
from src.classes.Charts import Charts
from src.classes.AI import AI

# Global vars
CSV_FILE_PATH = "../donnees/data_mining_DB_clients_tbl_bis.csv"
CSV_TRAINING_FILE_PATH = "../donnees/training_data.csv"


def calculate_resignation(file):
    """
    Calculer les démission et les non démission
    :param file:
    :return: N/A
    """

    labels_count = {
        'count_equal': 'Non démission',
        'count_not_equal': 'Démission',
    }
    count_args = {
        'colon': 'DTDEM',
        'value': '1900-12-31',
        'labels': labels_count
    }

    count_result = Stats.count_value(count_args, file)
    print(str(count_result))

    # Draw charts
    labels = []
    data = []

    for key, value in count_result.items():
        labels.append(key)
        data.append(value)

    Charts.draw_bars(labels, data)


def calculate_resignation_by_year(file):
    """
    Calculer les démission par an
    :param file:
    :return: N/A
    """
    count_args = {
        'colon': 'DTDEM',
        'value':  '1900-12-31',
    }
    count_result = Stats.count_by_year(count_args, file)

    # Draw charts
    labels = []
    data = []

    for key, value in sorted(count_result.items()):
        labels.append(key)
        data.append(value)

    args = {
        "x_data": labels,
        "y_data": data,
        "title": 'Démission par an',
        "xlabel": 'Année',
        "ylabel": 'Nombre de démission',
    }

    Charts.draw_line_chart(args)


def tain_ai():
    """
    :return:
    """
    # Get colons from file
    file = File(CSV_FILE_PATH)
    file.load_data_from_csv()
    colones = file.data[0]

    AI_ = AI(CSV_TRAINING_FILE_PATH, colones)
    AI_.train('CDMOTDEM')


def main():
    """
    Main function
    :return: status
    """
    file = File(CSV_FILE_PATH)
    file.load_data_from_csv()

    calculate_resignation(file)
    calculate_resignation_by_year(file)
    # file.adapt_to_training()
    # file.save_file(CSV_TRAINING_FILE_PATH)
    # tain_ai()


    return 0


if __name__ == "__main__":
    status = main()
