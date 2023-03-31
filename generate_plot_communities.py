import igraph as ig
import matplotlib.pyplot as plt
import config

g, _ = config.get_graph()

communities = g.community_edge_betweenness()
communities = communities.as_clustering()

num_c = len(communities)
palette = ig.RainbowPalette(n=num_c)

for i, community in enumerate(communities):
    g.vs[community]["color"] = i
    community_edges = g.es.select(_within=community)
    community_edges["color"] = i

fig, ax = plt.subplots()
ig.plot(
    communities,
    palette=palette,
    edge_width=1,
    target=f'{config.get_exit_dateformat()}_communities_graph.pdf',
    bbox=config.BOX_SIZE
)

print(f"---- {__file__} output generated ")



