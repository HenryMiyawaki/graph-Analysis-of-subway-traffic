
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

    def __init__(self, dataset, columns=None, keyword=None):
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

    def verifyIntegration(self, stationRow, stationCol, position):
        if stationRow == stationCol:
            count = 0
            for line in self.__dataset:
                for station in line[self.__keywords["station"]]:
                    count = count + 1
                    if station[self.__keywords["station_name"]] == stationRow and count != position:
                        return 1
        else:
            for line in self.__dataset:
                nextStation = False
                for station in line[self.__keywords["station"]]:
                    if nextStation and station[self.__keywords["station_name"]] == stationCol:
                        print(stationRow + " conecta com " + stationCol)
                        return 1
                    else:
                        nextStation = False

                    if station[self.__keywords["station_name"]] == stationRow:
                        nextStation = True
        return 0


table = RelationshipTable(data.SUBWAY_DATASET)

count = 0
matrix = []

for row in table.get_columns():
    aux = []
    count = count + 1
    for col in table.get_columns():
        aux.append(table.verifyIntegration(row, col, count))

    matrix.append(aux)

print(matrix)
