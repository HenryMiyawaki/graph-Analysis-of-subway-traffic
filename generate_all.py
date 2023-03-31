
import os

scripts = [
    "generate_plot_tree.py",
    "generate_plot_station.py",
    "generate_plot_sizeweight.py",
    "generate_plot_communities.py",
    "generate_plot_cluster.py",
    "generate_plot_closeness.py",
    "generate_plot_circle.py",
    "generate_plot_bridge.py",
    "generate_plot_betweenness.py",
    "generate_plot_articulation.py",
    "generate_relationship_table.py"
]

for script in scripts:
    os.system(f"/usr/local/bin/python3 {script}")