import igraph as ig
import matplotlib.pyplot as plt
import config 

g, _ = config.get_graph()
bridges = g.bridges()

g.es["color"] = "gray"
g.es[bridges]["color"] = "red"
g.es[bridges]["width"] = 1.2

fix, ax = plt.subplots()
ig.plot(
    g,
    target=f'{config.get_exit_dateformat()}_bridges.pdf',
    vertex_color=config.VERTEX_COLOR,
    bbox=config.BOX_SIZE
)

print(f"---- {__file__} output generated ")
