import igraph as ig
import matplotlib.pyplot as plt
import config


g, _= config.get_graph()

communities = g.community_edge_betweenness()
communities = communities.as_clustering()

num_communities = len(communities)
palette1 = ig.RainbowPalette(n=num_communities)
for i, community in enumerate(communities):
    g.vs[community]["color"] = i
    community_edges = g.es.select(_within=community)
    community_edges["color"] = i

g.vs["label"] = ["\n\n" + label for label in g.vs["label"]]

fix, ax = plt.subplots()
ig.plot(
    communities,
    target=f'{config.get_exit_dateformat()}_cluster.pdf',
    palette=palette1,
    mark_groups=True,
    bbox=config.BOX_SIZE
)

print(f"---- {__file__} output generated ")

