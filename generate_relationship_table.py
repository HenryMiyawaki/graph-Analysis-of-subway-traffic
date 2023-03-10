
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
            self.columns = self.get_columns()

    def get_columns(self):
        
        if self.__columns != None:
            return self.__columns

        cols = []
        for line in self.__dataset:
            for station in line[self.__keywords["station"]]:
                cols.append(station[self.__keywords["station_name"]])

        return cols



table = RelationshipTable(data.SUBWAY_DATASET)

count = 1
for station in table.get_columns():
    print(str(count) + " " + station)
    count += 1
