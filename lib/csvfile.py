# -*- coding: utf-8 -*-
#!/usr/bin/env python

import pandas
import csv


def rows_to_csv(filepath, rows, columns=[]):
    """
    Takes list of dictionaries and filepath and outputs a spreadsheet
    Params:
        rows(list):
            A list of dictionaries
        
        columns(list):
            A list of the key in the rows that you want to export in the csv file
            by default it will display all      
    """

    
def csv_to_rows(filepath):
    """
    Converts csv file to list of dicts.
    """
    
    df = pandas.read_csv(filepath)
    data = df.dropna(axis=0, subset=['Artist']).to_dict('records')
   
    return data
        