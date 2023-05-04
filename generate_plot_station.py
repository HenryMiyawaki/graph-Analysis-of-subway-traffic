import config

from igraph import Graph, plot

from logic.RelatioshipTable import RelationshipTable
from logic.StationDataset import StationDataset

g,_ = config.get_graph()
plot(g, target=f'{config.get_exit_dateformat()}_graph.pdf', bbox=config.BOX_SIZE)

print(f"---- {__file__} output generated ")