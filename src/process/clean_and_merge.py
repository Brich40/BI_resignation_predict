import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from datetime import datetime


def convert_to_categories(tlb_data, colons, status):
    """
    :param tlb_data:
    :param colons:
    :param status:
    :return:
    """
    if 'AGEAD' in colons:
        tlb_data['CATAGEAD'] = ''
        tlb_data['CATAGEAD'][tlb_data['AGEAD'] <=10] = '0_10'
        tlb_data['CATAGEAD'][(tlb_data['AGEAD'] > 10) & (tlb_data['AGEAD'] <= 20)] = '11_20'
        tlb_data['CATAGEAD'][(tlb_data['AGEAD'] > 20) & (tlb_data['AGEAD'] <= 30)] = '21_30'
        tlb_data['CATAGEAD'][(tlb_data['AGEAD'] > 30) & (tlb_data['AGEAD'] <= 40)] = '31_40'
        tlb_data['CATAGEAD'][(tlb_data['AGEAD'] > 40) & (tlb_data['AGEAD'] <= 50)] = '41_50'
        tlb_data['CATAGEAD'][(tlb_data['AGEAD'] > 50) & (tlb_data['AGEAD'] <= 60)] = '51_60'
        tlb_data['CATAGEAD'][(tlb_data['AGEAD'] > 60) & (tlb_data['AGEAD'] <= 70)] = '61_70'
        tlb_data['CATAGEAD'][(tlb_data['AGEAD'] > 70)] = '71_plus'

    if 'adh' in colons:
        tlb_data['CATadh'] = ''
        tlb_data['CATadh'][tlb_data['adh'] <=10] = '0_10'
        tlb_data['CATadh'][(tlb_data['adh'] > 10) & (tlb_data['adh'] <= 20)] = '11_20'
        tlb_data['CATadh'][(tlb_data['adh'] > 20) & (tlb_data['adh'] <= 30)] = '21_30'
        tlb_data['CATadh'][(tlb_data['adh'] > 30) & (tlb_data['adh'] <= 40)] = '31_40'
        tlb_data['CATadh'][(tlb_data['adh'] > 40) & (tlb_data['adh'] <= 50)] = '41_50'
        tlb_data['CATadh'][(tlb_data['adh'] > 50) & (tlb_data['adh'] <= 60)] = '51_60'
        tlb_data['CATadh'][(tlb_data['adh'] > 60) & (tlb_data['adh'] <= 70)] = '61_70'
        tlb_data['CATadh'][tlb_data['adh'] > 70] = '71_plus'

    if 'agedem' in colons:
        tlb_data['CATagedem'] = ''
        tlb_data['CATagedem'][tlb_data['agedem'] <=10] = '0_10'
        tlb_data['CATagedem'][(tlb_data['agedem'] > 10) & (tlb_data['agedem'] <= 20)] = '11_20'
        tlb_data['CATagedem'][(tlb_data['agedem'] > 20) & (tlb_data['agedem'] <= 30)] = '21_30'
        tlb_data['CATagedem'][(tlb_data['agedem'] > 30) & (tlb_data['agedem'] <= 40)] = '31_40'
        tlb_data['CATagedem'][(tlb_data['agedem'] > 40) & (tlb_data['agedem'] <= 50)] = '41_50'
        tlb_data['CATagedem'][(tlb_data['agedem'] > 50) & (tlb_data['agedem'] <= 60)] = '51_60'
        tlb_data['CATagedem'][(tlb_data['agedem'] > 60) & (tlb_data['agedem'] <= 70)] = '61_70'
        tlb_data['CATagedem'][tlb_data['agedem'] > 70] = '71_plus'

    if 'memberAge' in colons:
        tlb_data['CATmemberAge'] = ''
        tlb_data['CATmemberAge'][tlb_data['memberAge'] <= 10] = '0_10'
        tlb_data['CATmemberAge'][(tlb_data['memberAge'] > 10) & (tlb_data['memberAge'] <= 20)] = '11_20'
        tlb_data['CATmemberAge'][(tlb_data['memberAge'] > 20) & (tlb_data['memberAge'] <= 30)] = '21_30'
        tlb_data['CATmemberAge'][(tlb_data['memberAge'] > 30) & (tlb_data['memberAge'] <= 40)] = '31_40'
        tlb_data['CATmemberAge'][(tlb_data['memberAge'] > 40) & (tlb_data['memberAge'] <= 50)] = '41_50'
        tlb_data['CATmemberAge'][(tlb_data['memberAge'] > 50) & (tlb_data['memberAge'] <= 60)] = '51_60'
        tlb_data['CATmemberAge'][(tlb_data['memberAge'] > 60) & (tlb_data['memberAge'] <= 70)] = '61_70'
        tlb_data['CATmemberAge'][tlb_data['memberAge'] > 70] = '71plus'

    # Ajouter status (démissionnaire ou adhérent)
    tlb_data['statut'] = status


def clean_tbl(input, output):
    """
    :param input:
    :param output:
    :return:
    """
    print("Cleaning tlb file...")
    clients_tbl = pd.read_csv(input, sep=',')
    cols = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'DTDEM', 'CDMOTDEM', 'CDCATCL', 'AGEAD', 'agedem', 'adh']

    tlb_data = clients_tbl.get(cols)

    """
        donner des intervals d'age AGEAD, adh et agedem
    """

    convert_to_categories(tlb_data, ['AGEAD', 'adh', 'agedem'],status='demissionnaire')

    """
    Ajouter le statut pour idetifier les demissionnaire 
    et les adhérents dans le fichier résultat de merge
    """
    print("*-------------------------------*")
    print("===> Résultats tbl : ")
    print(tlb_data)

    tlb_data.to_csv(output, sep=",", index=False)


def clean_tbl_bis(input, output):
    tbl_bis_data = pd.read_csv(input, sep=',')

    """
    Supprimer les lignes avec les collones erronées:
    """
    clean_tlb_bis_data = tbl_bis_data.loc[(tbl_bis_data['DTNAIS'] != "0000-00-00") & (tbl_bis_data['DTNAIS'] != "1900-01-00") ]

    """
        Nettoyer les lignes avec les collones de motif de démission erronés:
    """
    clean_tlb_bis_data = tbl_bis_data.loc[((pd.notna(clean_tlb_bis_data['CDMOTDEM'])) & (tbl_bis_data['DTDEM'] != "1900-12-31")) | (pd.isna(clean_tlb_bis_data['CDMOTDEM']))]

    """
        Ajouter l'age de l'adherent lors de l'inscription dans sa banque
    """
    calcul_age_lamda = (lambda row: datetime.strptime(row['DTADH'], '%Y-%m-%d').year - datetime.strptime(row['DTNAIS'], '%Y-%m-%d').year)
    clean_tlb_bis_data["AGEAD"] = clean_tlb_bis_data.apply(calcul_age_lamda, axis=1)

    """
    Dans cette partie on divise les adhérents et les démissionnaires sur deux fichiers
    """
    tbl_adherents_data = clean_tlb_bis_data.loc[(pd.isna(clean_tlb_bis_data['CDMOTDEM']))]
    tlb_demission_data = clean_tlb_bis_data.loc[(pd.notna(clean_tlb_bis_data['CDMOTDEM']))]

    """
    Suppimer les colonne idetifiants au statut Adhérent/demissionnaire (DTDEM date démisson, CDMOTDEM et motif)
    """
    del tbl_adherents_data['CDMOTDEM']
    del tbl_adherents_data['DTDEM']

    """
    Corriger les lignes avec un CDMOTDEM valide et date erronée
    """
    tlb_demission_data['DTDEM'][(pd.notna(tlb_demission_data['CDMOTDEM'])) &
                                (tlb_demission_data['DTDEM'] == '1900-12-31')] = '2007-01-01'

    """
    Données supplimentaires 
        Pour tlb_demission_data : 
            agedem = age de démission
            adh = temps de fidilité du client

        Pour tbl_adherents_data : 
            memberAge = age d'adherent (2007 - DTNAIS)
            adh = temps de fidilité du client (2007 - DTADH)
    """

    tlb_demission_data["agedem"] = tlb_demission_data.apply(lambda row: datetime.strptime(row['DTDEM'], '%Y-%m-%d').year - datetime.strptime(row['DTNAIS'], '%Y-%m-%d').year, axis=1)
    tlb_demission_data["adh"] = tlb_demission_data.apply(lambda row: datetime.strptime(row['DTDEM'], '%Y-%m-%d').year - datetime.strptime(row['DTADH'], '%Y-%m-%d').year, axis=1)
    tbl_adherents_data["memberAge"] = tbl_adherents_data.apply(lambda row: datetime.strptime('2007-01-01', '%Y-%m-%d').year - datetime.strptime(row['DTNAIS'], '%Y-%m-%d').year, axis=1)
    tbl_adherents_data["adh"] = tbl_adherents_data.apply(lambda row: datetime.strptime('2007-01-01', '%Y-%m-%d').year - datetime.strptime(row['DTADH'], '%Y-%m-%d').year, axis=1)

    convert_to_categories(tlb_demission_data, ['AGEAD', 'adh', 'agedem'], status='demissionnaire')
    convert_to_categories(tbl_adherents_data, ['AGEAD', 'adh', 'memberAge'], status='adherent')


    """
    Selectionner les collones :
    """
    #  Pour les adherents :
    cols_adherent = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'CDCATCL', 'AGEAD', 'memberAge', 'adh', 'CATAGEAD', 'CATmemberAge', 'CATadh', 'statut']

    #  Pour les démessionnaires :
    cols_demissionnaire = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'DTDEM', 'CDMOTDEM', 'CDCATCL', 'AGEAD', 'agedem', 'adh', 'CATAGEAD', 'CATagedem', 'CATadh', 'statut']


    tbl_adherents_data = tbl_adherents_data[cols_adherent]
    tlb_demission_data = tlb_demission_data[cols_demissionnaire]

    tbl_adherents_data.to_csv('../../donnees/merge/adherent.csv', sep=",", index=False)
    tlb_demission_data.to_csv('../../donnees/clean/data_mining_DB_clients_tbl_bis_demission_clean.csv', sep=",", index=False)

    print("*-------------------------------*")
    print("===> Résultats tbl bis: ")
    print(tbl_adherents_data)
    print(tlb_demission_data)


def merge_demission(input1, input2, output):
    tlb_demission = pd.read_csv(input1, sep=',')
    tlb_bis_demission = pd.read_csv(input2, sep=',')

    # Supprimer les idetifiants
    del tlb_demission['Id']
    del tlb_bis_demission['Id']
    fusion_dem = pd.DataFrame(tlb_demission).append(pd.DataFrame(tlb_bis_demission))

    fusion_dem.to_csv(output, sep=",", index=False)


if __name__ == "__main__":
    tbl_input_path = "../../donnees/data_mining_DB_clients_tbl.csv"
    tbl_output_path = "../../donnees/clean/data_mining_DB_clients_tbl_clean.csv"
    clean_tbl(tbl_input_path, tbl_output_path)

    tbl_bis_input_path = "../../donnees/data_mining_DB_clients_tbl_bis.csv"
    tbl_bis_output_path = "../../donnees/clean/data_mining_DB_clients_tbl_bis_clean.csv"
    clean_tbl_bis(tbl_bis_input_path, tbl_bis_output_path)

    # Merge
    input1 = '../../donnees/clean/data_mining_DB_clients_tbl_clean.csv'
    input2 = '../../donnees/clean/data_mining_DB_clients_tbl_bis_demission_clean.csv'

    out_put = '../../donnees/merge/demissionnaire.csv'
    merge_demission(input1, input2, out_put)