#!/usr/bin/env python
import lib.csvfile as svc
from collections import Counter


def create_new_stock_numbers():
    """
    Uses methods from the csv library to read data from
    a csv and create a new csv with updated stock numbers.
    New stock numbers generated using artists' initials(prefix)
    and existing number(suffix).
    """
    data = svc.csv_to_rows("data/artworks.csv")
    artist_names = [row["Artist"] for row in data]
    names_counter = Counter(artist_names)
    stock_prefixes = []
    row = 0
    for artist_name in names_counter:
        full_name = artist_name.split()
        stock_prefix = ""
        if len(full_name) == 1:
            stock_prefix = full_name[0:2].upper()
        elif len(full_name) > 1:
            stock_prefix = full_name[0][0].upper() + full_name[-1][0].upper()

        if stock_prefix in stock_prefixes:
            fname = full_name[0]
            for i in range(len(fname) - 1):
                stock_prefix = fname[0] + fname[i + 1].upper()
                if stock_prefix not in stock_prefixes:

                    for i in range(names_counter[artist_name]):
                        stock_number = stock_prefix + " " + str(i + 1).zfill(3)
                        data[row]["Stock number"] = stock_number
                    break
                stock_prefixes.append(stock_prefix)
        else:
            stock_prefixes.append(stock_prefix)

        for i in range(names_counter[artist_name]):
            stock_number = stock_prefix + " " + str(i + 1).zfill(3)
            data[row]["Stock number"] = stock_number
            row += 1

    return data


rows = create_new_stock_numbers()
new_csv_path = "data/new_artworks.csv"
svc.rows_to_csv(new_csv_path, rows)
