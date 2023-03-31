import igraph as ig
import matplotlib.pyplot as plt

from datetime import datetime
from logic.get_station_graph import get_station_graph

g = get_station_graph(["merge_duplicated", ["turnoff_interception"]])
articulation_points = g.vs[g.articulation_points()]

analytis_report = { 
    "__metadata": {
        "__dataset": {},
        "__matrix": {}
    },
    "graph": {
        "articulation_points": g.articulation_points(),
        "spanning_tree": g.spanning_tree(weights=None, return_tree=False),
        "community_edge_betweeness": g.community_edge_betweenness(),
        "communities": g.community_edge_betweenness().as_clustering(),
        "bridges": g.bridges(),
        "vertex_betweenness": g.betweenness(),
        "edge_betweenness": g.edge_betweenness(),
        "closeness": g.closeness
    }
}

print(analytis_report)