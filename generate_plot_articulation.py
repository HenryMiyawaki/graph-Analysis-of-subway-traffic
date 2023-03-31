import igraph as ig
import matplotlib.pyplot as plt
import config

g, _ = config.get_graph()
articulation_points = g.vs[g.articulation_points()]

fix, ax = plt.subplots()
ig.plot(
    g,
    target=f'{config.get_exit_dateformat()}_articulation_points_graph.pdf',
    vertex_color=config.VERTEX_COLOR,
    vertex_frame_color = ["red" if v in articulation_points else "black" for v in g.vs],
    vertex_frame_width = [3 if v in articulation_points else 1 for v in g.vs],
    edge_color='gray',
    bbox=config.BOX_SIZE
)

print(f"---- {__file__} output generated")