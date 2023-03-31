
import config

from openpyxl import Workbook

table = config.get_relationship_table()

relation_text = table.transform_text(table.get_matrix(), top_columns=True)
filename = f'{config.get_exit_dateformat()}_relationship_table.csv'

wb = Workbook()
ws = wb.active

for i, line in enumerate(relation_text.splitlines()):
    columns = line.split(',')
    for j, column in enumerate(columns):
        ws.cell(row=i+1, column=j+1, value=column)

if config.SAVE:
    wb.save(f"./data/output/adjascenty_matrix/{filename}.xlsx")
    if config.SUPRESS_OUTPUT:
        print("---- output generated on ./data/output/adjascenty_matrix/ directory")