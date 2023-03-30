import igraph as ig
import matplotlib.pyplot as plt

from datetime import datetime
from logic.get_station_graph import get_station_graph

g = get_station_graph(["merge_duplicated", "turnoff_interception"])
articulation_points = g.vs[g.articulation_points()]

fix, ax = plt.subplots()
ig.plot(
    g,
    target=f'{datetime.now().strftime("%d_%m_%Y_%S")}_articulation_points_graph.pdf',
    vertex_color="lightblue",
    vertex_frame_color = ["red" if v in articulation_points else "black" for v in g.vs],
    vertex_frame_width = [3 if v in articulation_points else 1 for v in g.vs],
    edge_color='gray',
    bbox=(8000,8000)
)