""" datasets.py
    
    Implement a helper funciton to load in these regression datasets for 
    TP02.
"""
import pandas as pd
import numpy as np


def dataset_load(set_name):
    """ dataset_load(set_name)

        Given a particular dataset string name, load testing and traing data.
    """
    data_file = 'mldata/%s.data' % set_name

    if set_name == 'laozone':
        # This dataset is already in good form for importing
        df = pd.read_csv(data_file)
    elif set_name == 'wpbc':
        field_names = ['id', 'outcome', 'time', 
                       'radiusA', 'textureA', 'perimeterA', 'areaA', 'smoothnessA',
                       'compactnessA', 'concavityA', 'concaveptsA', 'symmetryA', 'fdimA',
                       'radiusB', 'textureB', 'perimeterB', 'areaB', 'smoothnessB',
                       'compactnessB', 'concavityB', 'concaveptsB', 'symmetryB', 'fdimB',
                       'radiusC', 'textureC', 'perimeterC', 'areaC', 'smoothnessC',
                       'compactnessC', 'concavityC', 'concaveptsC', 'symmetryC', 'fdimC',
                       'tumorsize', 'lymphstat']
        df = pd.read_csv(data_file, header=-1, names=field_names)
    elif set_name == 'saheart':
        df = pd.read_csv(data_file)
        del df['row.names']
    elif set_name == 'prostate':
        df = pd.read_csv(data_file, sep='\t')
        del df['row']
    elif set_name == 'bone':
        df = pd.read_csv(data_file, sep='\t')
    else:
        df = pd.DataFrame()

    return df

def dataset_info(set_name):
    """ dataset_info(set_name)

        Given a particular dataset string name, print out the information about
        this particular dataset.
    """
    with open('mldata/%s.info' % set_name, 'r') as info_file:
        for line in info_file.readlines():
            print(line.strip())
