import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

adjmat = open('adj_matrix_Snowden2.txt', 'r')


for line in adjmat:
    line = line.strip()
    columns = line.split()
    i = columns[0]
    j = columns[1]
    w = columns[2]
    G.add_edge(i, j, weight=w)

# nx.draw(G)
# plt.show()


pos = nx.spring_layout(G)
nx.draw(G, pos, node_color='#A0CBE2', edge_color='#BB0000', width=2, edge_cmap=plt.cm.Blues, with_labels=True)
plt.show()
# plt.savefig("graph.png", dpi=500, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1)

adjmat.close()

