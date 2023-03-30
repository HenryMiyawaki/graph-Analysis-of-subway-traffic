import igraph as ig
import matplotlib.pyplot as plt

from datetime import datetime
from logic.get_station_graph import get_station_graph

g = get_station_graph(["merge_duplicated", "turnoff_interception"])
layout = g.layout("grid")

spanning_tree = g.spanning_tree(weights=None, return_tree=False)
fig, ax = plt.subplots()

print(spanning_tree)

g.es["color"] = "lightgray"
g.es[spanning_tree]["color"] = "midnightblue"
g.es["width"] = 0.5
g.es[spanning_tree]["width"] = 3.0

ig.plot(
    g,
    target=f'{datetime.now().strftime("%d_%m_%Y_%S")}_tree_graph.pdf',
    layout=layout,
    vertex_color="lightblue",
    edge_width=g.es["width"],
    bbox=(8000, 8000)
)