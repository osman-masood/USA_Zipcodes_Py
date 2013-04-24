# -*- coding: utf-8 -*-

__author__ = 'oamasood'


def get_zipcodes():
    import urllib2
    import zipfile
    from StringIO import StringIO

    url = "http://www.boutell.com/zipcodes/zipcode.zip"

    # Unzip file and get zipcode.csv file
    zfobj = zipfile.ZipFile(StringIO(urllib2.urlopen(url).read()))
    zipcode_csv = zfobj.open('zipcode.csv')
    zfobj.close()

    csv_table = convert_csv_to_table(StringIO(zipcode_csv.read()))
    zipcode_csv.close()

    # Get data & store into array
    return_table = []
    for row in csv_table:
        try:  # if invalid row, float(latitude) will throw an exception & row will not be inserted.
            code, city, state_code, latitude, longitude, timezone, is_dst_observed = row
            return_table.append(dict(
                zip=code,
                city=city,
                state=state_code,
                latitude=float(latitude),
                longitude=float(longitude),
                timezone=int(timezone),
                is_dst_observed=is_dst_observed == "1"
            ))
        except:
            pass
    return return_table


# convert uploaded csv file to Python table object (array of arrays)
def convert_csv_to_table(csv_file):
    import csv
    catalog = None
    new_catalog = []  # No friggin' idea why, but catalog doesn't let you iterate over it twice. That's why we need new_catalog
    try:
        # Guess dialect with sniffer and read in CSV
        dialect = csv.Sniffer().sniff(csv_file.readline())
        csv_file.seek(0)
        catalog = csv.reader(csv_file.read().splitlines(), dialect=dialect)
        csv_table = []

        # First, count maximum number of columns in any row. This will be # of cols in table
        num_columns = 0
        for row in catalog:
            if len(row) > num_columns: num_columns = len(row)
            new_catalog.append(row)

        # Make new candidates from CSV results
        for row in new_catalog:
            row_array = []
            is_row_empty = True
            for column_index in range(num_columns):  # 0, ..., num_columns-1
                column = row[column_index] if len(row) > column_index else ''
                if column: is_row_empty = False  # to ignore empty rows
                row_array.append(column.strip(' '))
            if not is_row_empty: csv_table.append(row_array)
    except Exception:
        csv_table = []
    return csv_table


