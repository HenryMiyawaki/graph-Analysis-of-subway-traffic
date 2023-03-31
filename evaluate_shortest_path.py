
import config
from igraph import Graph, plot

g, table = config.get_graph()
cols  = table.get_columns()

current_station = int( cols.index( input("Type the current station: ") ))
target_station = int( cols.index( input("Type the targe station: ") ) )

results = None
weights = config.get_weights()


if config.USE_WEIGHT == 0:
    results = g.get_shortest_paths(current_station, target_station, output="vpath")
    if len(results[0]) > 0:
        print("Shortest distance is: ", len(results[0])-1)
else:
    
    g.es["weight"] = weights
    results = g.get_shortest_paths(0, to=5, weights=g.es["weight"], output="epath")

    if len(results[0]) > 0:
        distance = 0
        for e in results[0]:
            distance += g.es[e]["weight"]
        print("Shortest weighted distance is: ", distance)


for node_index in results:
    print(cols[node_index])
    