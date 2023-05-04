import config

g, h = config.get_graph()

print(g.community_edge_betweenness().as_clustering())