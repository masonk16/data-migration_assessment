# -*- coding: utf-8 -*-
#!/usr/bin/env python

import pandas


def rows_to_csv(filepath, rows):
    """
    Takes list of dictionaries and filepath and outputs a spreadsheet
    Params:
        rows(list):
            A list of dictionaries

        filepath:
            path to create new csv with updated stock numbers
    """
    df = pandas.DataFrame.from_dict(rows)
    updated_csv = df.to_csv(filepath, index=False, header=True)

    return updated_csv


def csv_to_rows(filepath):
    """
    Converts csv file to list of dicts.
    """

    df = pandas.read_csv(filepath)
    data = df.dropna(axis=0, subset=["Artist"]).to_dict("records")

    return data
