import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

"""変更部分↓
capacity=辺容量, add_weighted_..=(u,v,uvの重み)
供給点はdemandを負に, 需要点は正に指定
posはplotした時の頂点座標を指定.(面倒ならpos=nx.spring_layout(G)でいい感じになる)
"""
G.add_node(0, demand=-3)
G.add_node(3, demand=3)
capacity ={(0,1): 2, (0,2): 2, (1,3): 2, (1,2): 2, (2,3): 2}
G.add_weighted_edges_from([(0,1,2),(0,2,1),(1,2,1),(1,3,2),(2,3,4)])
pos ={0:(0,1),1:(1,2),2:(1,0),3:(2,1)}

# ここから変えない.
for (i,j) in G.edges():
    G[i][j]["capacity"] = capacity[i,j]
edge_labels = {}
for (i,j) in G.edges():
    edge_labels[i,j] = f"cost={ G[i][j]['weight'] }\ncap={ G[i][j]['capacity']}"
plt.figure()
nx.draw(G, pos=pos,with_labels=True, node_size=1000)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
plt.show()

cost, flow = nx.algorithms.flow.network_simplex(G)
edge_color = []
for i in G.nodes():
    for j in flow[i]:
        color = "blue" if flow[i][j] else "gray"
        edge_labels[i,j] = f"f={flow[i][j]}"
        edge_color.append(color)

plt.figure()
nx.draw(G, pos=pos,with_labels=True, node_size=1000,edge_color=edge_color)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
plt.show()
