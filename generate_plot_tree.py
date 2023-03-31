import config
import igraph as ig
import matplotlib.pyplot as plt

from datetime import datetime

g, _ = config.get_graph()
layout = g.layout("grid")

spanning_tree = g.spanning_tree(weights=None, return_tree=False)
fig, ax = plt.subplots()

g.es["color"] = "lightgray"
g.es[spanning_tree]["color"] = "midnightblue"
g.es["width"] = 0.5
g.es[spanning_tree]["width"] = 3.0

ig.plot(
    g,
    target=f'{config.get_exit_dateformat()}_tree_graph.pdf',
    layout=layout,
    vertex_color=config.VERTEX_COLOR,
    edge_width=g.es["width"],
    bbox=config.BOX_SIZE
)

print(f"---- {__file__} output generated ")