# Fix matrix station key name

Status: Done

```python
filename = f'{datetime.now().strftime("%d_%m_%Y_%s")}_relationship_table.csv'

wb = Workbook()
ws = wb.active

for i, line in enumerate(relation_text.splitlines()):
    columns = line.split(',')
    for j, column in enumerate(columns):
        ws.cell(row=i+1, column=j+1, value=column)

wb.save(f"./output/{filename}.xlsx")
```