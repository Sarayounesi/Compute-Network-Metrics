import networkx as nx
import networkx
import matplotlib.pyplot as plt
import pylab as plt

G = nx.Graph()
G.add_edges_from([('SaraYounesi', 'Abed Ebadi',{'weight': 100}), ('SaraYounesi', 'Nezakati',{'weight': 200}), ('Nezakati', 'Abed Ebadi',{'weight': 300}), ('Deniz Ahmadi', 'Abed Ebadi',{'weight': 300}), ('Deniz Ahmadi', 'kia',{'weight': 100}),
                 ('mamad', 'arshia',{'weight': 100}), ('SaraYounesi', 'kia',{'weight': 400}), ('AliSalimi', 'mamad'  ,{'weight': 100}), ('kia', 'arshia',{'weight': 200}), ('AliSalimi', 'Aria',{'weight': 100}) ,('mamad', 'Amiri',{'weight': 300}) ,('mamad', 'pakdaman',{'weight': 100}),('mamad', 'hanie',{'weight': 100}),('hanie', 'narges',{'weight': 100}) ,('narges', 'pakdaman',{'weight': 100}),('hanie', 'sana',{'weight': 100}) ,('Amiri', 'sana',{'weight': 100})])

plt.figure() 
plt.grid(True)


pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500, node_color='red')
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()


def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()


plot_degree_dist(G)


print("--------------------------------------------------------------------------------------------------------------")
print("2.View Of network IUST Student")
print("--------------------------------------------------------------------------------------------------------------")
print(G)
print('1.Number of nodes', len(G.nodes))
print('2.Number of edges', len(G.edges))
print('3.Average degree', sum(dict(G.degree).values()) / len(G.nodes))
print('Density of graph', ((len(G.edges) / (len(G.nodes) * (len(G.nodes) - 1)))))
print('Clustering coefficient 1', nx.clustering(G))
print('Clustering coefficient 2', list(nx.triangles(G, (0, 1)).values()))
print('Diametr',  max([max(j.values())
      for (i, j) in nx.shortest_path_length(G)]))
print('Avrage shortest path', (nx.average_shortest_path_length(G)))
print('Assortativity (Degree Correlation) ',
      nx.degree_assortativity_coefficient(G))
print('Find top 5 nodes based on 3 different centrality measures ',
      nx.degree_centrality(G))
print('Network Centralization', nx.eigenvector_centrality(G))
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")