
import config

g, table = config.get_graph()
cols = table.get_columns()

ls = list()

for i, x in cols:
    ls.append( g.vs[i].degree() )

print(ls)