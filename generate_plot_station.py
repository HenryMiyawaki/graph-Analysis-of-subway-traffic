
from datetime import datetime
from dataset import data
from logic.RelatioshipTable import RelationshipTable
from igraph import Graph, plot

import sys

table = RelationshipTable(data.SUBWAY_DATASET)
table = table.evaluate_matrix()

for arg in sys.argv[1:]:
    func = getattr(table, arg)
    if func != None:
        table = func()

mx = table.get_matrix()

g = Graph.Incidence(mx)
g.vs["label"] = table.get_columns()

plot(g, target=f'{datetime.now().strftime("%d_%m_%Y_%S")}_graph.pdf', bbox=(8000, 8000))
