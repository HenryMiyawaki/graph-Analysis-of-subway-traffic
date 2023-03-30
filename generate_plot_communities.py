import igraph as ig
import matplotlib.pyplot as plt

from datetime import datetime
from logic.get_station_graph import get_station_graph

g = get_station_graph(["merge_duplicated", "turnoff_interception"])

communities = g.community_edge_betweenness()
print(communities)
communities = communities.as_clustering()
print(communities)

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
    target=f'{datetime.now().strftime("%d_%m_%Y_%S")}_communities_graph.pdf',
    bbox=(8000, 8000)
)




