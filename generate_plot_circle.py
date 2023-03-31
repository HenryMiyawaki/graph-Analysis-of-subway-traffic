
import matplotlib.pyplot as plt
import numpy as np
import config

from igraph import Graph, plot

g,_ = config.get_graph()

layout = g.layout('circle')

fix, ax = plt.subplots()
g.es["weight"] = config.get_weights()

plot(
    g,
    layout=layout,
    target=f'{config.get_exit_dateformat()}_circle.pdf',
    vertex_color="lightblue",
    bbox=config.BOX_SIZE
)

print(f"---- {__file__} output generated ")
