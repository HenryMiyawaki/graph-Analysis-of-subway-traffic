import igraph as ig
import matplotlib.pyplot as plt
import config

from logic.plot_betweenness import plot_betweenness

g, _  = config.get_graph()

vertex_betweenness1 = g.betweenness()
edge_betweenness1 = g.edge_betweenness()

fig, axs = plt.subplots(
    3, 2,
    figsize=(7, 6),
    gridspec_kw=dict(height_ratios=(20, 1, 1)),
)

plot_betweenness(g, vertex_betweenness1, edge_betweenness1, *axs[:, 0], target=f'{config.get_exit_dateformat()}_betweenness.pdf', bbox=config.BOX_SIZE)

print(f"---- {__file__} output generated")