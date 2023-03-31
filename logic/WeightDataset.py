
from logic.Dataset import Dataset
from logic.RelatioshipTable import RelationshipTable
from logic.StationDataset import StationDataset


class WeightDataset(StationDataset):

    def __init__(self, correlated_table: RelationshipTable, format: str, location="./") -> None:
        self.__correlated_table = correlated_table
        super().__init__(format, location)

    def get_ordered_correlated_index(self, index_key, normalized=False) -> list:

        cols = self.__correlated_table.get_columns()
        ordered_weights = list()
        self.data = self.get_dictionary()

        for index, key in enumerate(cols):
            try:
                ordered_weights.append(self.data[key][index_key])
            except KeyError as e :
                print(f"error on {index} - {key} ")
        
        if normalized:
            ordered_weights = self.normalized(ordered_weights)

        return ordered_weights

    def normalized(self, ls: list):

        top = max(ls)
        ls = map(lambda x: x/top, ls)

        return list(ls)
