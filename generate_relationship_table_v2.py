
from os import stat
import sys
import pandas as pd
from dataset import data


KEYWORDS = {
    "line": "Linha",
    "station": "Estacoes",
    "station_name": "Estação"
}

class RelationshipTable():

    __dataset = None
    __columns = None
    __keywords = None
    def __init__(self, dataset, columns = None, keyword = None):
        self.__dataset = dataset

        if keyword == None:
            self.__keywords = KEYWORDS

        if columns == None:
            self.__columns = self.get_columns()

    def get_columns(self):
        
        if self.__columns != None:
            return self.__columns

        cols = []
        for line in self.__dataset:
            for station in line[self.__keywords["station"]]:
                cols.append(station[self.__keywords["station_name"]])

        return cols

    def evaluate_matrix(self):

        mx_cols = self.__columns
        mx_lines = self.__columns

        last_station = None
        next_station = None
        mx = []

        if (mx_cols == None) or (mx_lines == None):
            cols = self.get_columns()
            lines = cols

        for i,c in enumerate(mx_cols):
            mx.append([])
            for l in mx_lines:
                mx[i].append(0)


        for idx_col, col in enumerate(mx_cols):
            for idx_lines, line in enumerate(mx_lines):
    
                station_line = mx_cols[idx_col]
                station_col = mx_lines[idx_lines]
              
                if (station_line == station_col):
                    
                    mx[idx_col][idx_lines] = 1

                    if (len(mx[idx_col]) != idx_lines + 1):
                        mx[idx_col][idx_lines + 1] = 1
                    if (idx_lines != 0):
                        mx[idx_col][idx_lines - 1] = 1

            
        
        return mx

    def transform_dataframe(self):
        mx = self.evaluate_matrix()
        data = {}

        for i, columns in enumerate(mx):
            data[self.__columns[i]] = columns

        df = pd.DataFrame(data, index=self.__columns)
        return df

    def tranform_csv():
        pass


table = RelationshipTable(data.SUBWAY_DATASET)
cols = table.get_columns()
df = table.transform_dataframe()
df.to_excel("./relationship.xlsx")

_cols = []

for c in cols:
    c = c.replace("Estação", "Estacao") 
    c = c.replace("çã", "ca")
    c = c.replace("ã", "a")
    c = c.replace("ç", "c")
    c = c.replace("é", "e")
    c = c.replace("ê", "e")
    c = c.replace("É", "e")
    c = c.replace("í", "i")
    c = c.replace("á", "a")
    c = c.replace("Á", "A")
    c = c.replace("ó", "o")
    c = c.replace("Ó", "O")
    c = c.replace("ô", "o")
    c = c.replace("ú", "u")
    c = c.replace("Ú", "U")
    c = c.replace("-", "")

    _cols.append(c)
    

print(_cols)
mx = table.evaluate_matrix()

for i, item in  enumerate(mx):
    print(f"{_cols[i]}," + str(item)[1:len(str(item)) - 1])