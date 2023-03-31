
import matplotlib.pyplot as plt
import numpy as np
import config

from igraph import plot

g,_ = config.get_graph()

vertex_size = g.closeness()
vertex_size = [9000 * v**2 if not np.isnan(v) else 4000 for v in vertex_size]

fix, ax = plt.subplots()
g.es["weight"] = config.get_weights()

plot(
    g,
    target=f'{config.get_exit_dateformat()}_closeness.pdf',
    vertex_color=config.VERTEX_COLOR,
    vertex_size=vertex_size,
    bbox=config.BOX_SIZE
)

print(f"---- {__file__} output generated ")
