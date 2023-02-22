#! /usr/bin/env python3
# A script that imports movie data and finds the top-5 highest grossing movies
import csv


def find_top_5(filename):
    """Finds the top 5 highest grossing movies in a CSV dataset."""
    with open(filename) as f:
        csvr = csv.DictReader(f)
        rows = [r for r in csvr]
    
    gross_sort = lambda x : x["Gross"]
    rows.sort(key=gross_sort)
    top_five = rows[:-5:-1]

    for row in top_five:
        print("{row[Title]} ({row[Release Date]}) - ${row[Gross]}".format(
            row=row))

if __name__ == "__main__":
    find_top_5("Movies_gross_rating.csv")
