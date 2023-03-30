

from igraph import Graph, plot

from logic.RelatioshipTable import RelationshipTable
from logic.StationDataset import StationDataset

## move to a config file

DATASET_LOCATION = "./dataset/station"
DATASET_FORMAT = "json"

def get_station_graph(table_args: list) -> Graph:

    table = RelationshipTable(StationDataset(format=DATASET_FORMAT, location=DATASET_LOCATION).get_dictionary())
    table = table.evaluate_matrix()

    for arg in table_args:
        try:
            func = getattr(table, arg)
            if func != None:
                table = func()
        except Exception as e:
            print(e)

    # should be setted on a config formation file
    table = table.arrow_link("Estação Consolação->Estação Paulista")
    mx = table.get_matrix()

    # could be defined by parameters
    g = Graph.Adjacency(mx, mode="undirected")
    g.vs["label"] = table.get_columns()

    return g