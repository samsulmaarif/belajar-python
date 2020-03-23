from pathlib import Path
import csv
from collections import OrderedDict


def get_fuel_use(source_path):
    with source_path.open() as source_file:
        rdr = csv.DictReader(source_file)
        od = (OrderedDict([(column, row[column]) for column in rdr.fieldnames])
              for row in rdr)
        data = list(od)
    return data


source_path = Path("data.csv")
fuel_use = get_fuel_use(source_path)

print('date', 'start', 'end', 'depth', sep=" | ")
print(fuel_use)

# for leg in fuel_use:
#     start = float(leg['fuel height on'])
#     finish = float(leg['fuel height off'])
#     print("on", leg['date'], 'from', leg['engine on'], 'to', leg['engine off'],
#           'change', start - finish, 'in.')

