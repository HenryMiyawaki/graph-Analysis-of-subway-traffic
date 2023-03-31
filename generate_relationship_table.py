
import sys
from datetime import datetime

from openpyxl import Workbook

from dataset import data
from logic.RelatioshipTable import RelationshipTable
from logic.StationDataset import StationDataset

DATASET_LOCATION = "./dataset/station"
DATASET_LOCATION_PROJECTION = "./dataset/projection"
DATASET_FORMAT = "json"

join_dict = StationDataset(
    format=DATASET_FORMAT, location=DATASET_LOCATION).get_dictionary() + StationDataset(
    format=DATASET_FORMAT, location=DATASET_LOCATION_PROJECTION).get_dictionary()

table = RelationshipTable(join_dict)
table = table.evaluate_matrix()

for arg in sys.argv[1:]:
    try:
        func = getattr(table, arg)
        if func != None:
            table = func()
    except AttributeError as e:
        pass

relation_text = table.transform_text(table.get_matrix(), top_columns=True)
filename = f'{datetime.now().strftime("%d_%m_%Y")}_{datetime.now().microsecond}_relationship_table.csv'

wb = Workbook()
ws = wb.active

for i, line in enumerate(relation_text.splitlines()):
    columns = line.split(',')
    for j, column in enumerate(columns):
        ws.cell(row=i+1, column=j+1, value=column)

if "save" in sys.argv[1:]:
    wb.save(f"./data/output/adjascenty_matrix/{filename}.xlsx")
    print("---- output generated on ./data/output/adjascenty_matrix/ directory")
