import matplotlib.pyplot as plt
import numpy as np
import config

from igraph import Graph, plot

from datetime import datetime

weight = config.get_weights(normalized=True)
g, _ = config.get_graph()

vertex_size = [500*v*2 if not np.isnan(v) else 250 for v in weight]
vertex_size = [20 if v < 20 else v for v in weight]
vertex_size = [100 if v > 100 else v for v in weight]

fix, ax = plt.subplots()
g.es["weight"] = weight

plot(
    g,
    target=f'{config.get_exit_dateformat()}_sizeweight.pdf',
    vertex_color=config.VERTEX_COLOR,
    vertex_size=vertex_size,
    bbox=config.BOX_SIZE
)

print(f"---- {__file__} output generated ")
