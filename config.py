import sys

from igraph import Graph
from datetime import datetime
from logic.RelatioshipTable import RelationshipTable
from logic.StationDataset import StationDataset
from logic.WeightDataset import WeightDataset

DATASET_LOCATION = "./dataset/station"
WEIGHT_LOCATION = "./dataset/passagers_by_station_processed"

DATASET_FORMAT = "json"

USE_PROJECTION = False
USE_WEIGHT = True
SUPRESS_OUTPUT = True

ARGS = sys.argv

TABLE_METHODS = ["evaluate_matrix", "merge_duplicated", "turnoff_interception"]

DATE_EXIT = "%d_%m_%Y"

SAVE = True

BOX_SIZE = (8000, 8000)
VERTEX_COLOR = "lightblue"

def get_exit_dateformat():
    return f"{datetime.now().strftime(DATE_EXIT)}_{datetime.now().microsecond}"

def get_dataset():
    if USE_PROJECTION:
        return None
    else:
        return StationDataset(format=DATASET_FORMAT, location=DATASET_LOCATION).get_dictionary()

def get_relationship_table():
    table = RelationshipTable(get_dataset())
    for arg in TABLE_METHODS:
        try:
            func = getattr(table, arg)
            if func != None:
                table = func()
        except AttributeError as e:
            print("method doenst exist on table")

    table = table.arrow_link("Estação Consolação->Estação Paulista")
    return table

def get_graph():
    
    table = get_relationship_table()
    mx = table.get_matrix()

    g = Graph.Adjacency(mx, mode="undirected")
    g.vs["label"] = table.get_columns()

    return g, table

def get_weights(normalized = False):
    obj = WeightDataset(format=DATASET_FORMAT, location=WEIGHT_LOCATION, correlated_table=get_relationship_table())
    weights = obj.get_ordered_correlated_index(index_key="Média Diária", normalized=normalized)
    return weights