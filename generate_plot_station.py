
from dataset import data
from logic.RelatioshipTable import RelationshipTable
from igraph import Graph, plot

table = RelationshipTable(data.SUBWAY_DATASET)
table = table.evaluate_matrix()
table = table.merge_duplicated()
table = table.turnoff_interception()


mx = table.get_matrix()

g = Graph.Incidence(mx)
g.vs["label"] = table.get_columns()

plot(g, target='./myfile.pdf', bbox=(8000, 8000))
