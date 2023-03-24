
from datetime import datetime
from dataset import data
from openpyxl import Workbook
from logic.RelatioshipTable import RelationshipTable
from openpyxl import Workbook


table = RelationshipTable(data.SUBWAY_DATASET)
table = table.evaluate_matrix()
table = table.merge_duplicated()

relation_text = table.transform_text(table.get_matrix(), top_columns=True)
filename = f'{datetime.now().strftime("%d_%m_%Y_%s")}_relationship_table.csv'

wb = Workbook()
ws = wb.active

for i, line in enumerate(relation_text.splitlines()):
    columns = line.split(',')
    for j, column in enumerate(columns):
        ws.cell(row=i+1, column=j+1, value=column)

wb.save(f"./output/{filename}.xlsx")
print("---- output generated on ./output directory")
