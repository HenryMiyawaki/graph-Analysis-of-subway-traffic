
from os import stat
import sys
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

                    print(station_line)
                    mx[idx_col][idx_lines] = 1

                    if (len(mx[idx_col]) != idx_lines + 1):
                        mx[idx_col][idx_lines + 1] = 1
                    if (idx_lines != 0):
                        mx[idx_col][idx_lines - 1] = 1


        
        return mx


    # depracated method
    def is_parent_station(self, station_1, station_2):

    
        next_station = {}
        last_station = {}

        for line in self.__dataset:
            stations = line[self.__keywords["station"]]
            for idx, station in enumerate(stations):

                if (len(stations) == idx + 1):
                    next_station = {  }
                else:
                    next_station = stations[idx + 1]

                if (station[self.__keywords["station_name"]] == station_1):
                    return next_station.get(self.__keywords["station_name"], None) == station_2 or last_station.get(self.__keywords["station_name"], None)== station_2

                last_station = station
            last_station = { }
                
        return False
                


table = RelationshipTable(data.SUBWAY_DATASET)
cols = table.get_columns()
mx = table.evaluate_matrix()

for i,n in enumerate(mx[8]):
    if n == 1:
        print(cols[i])
