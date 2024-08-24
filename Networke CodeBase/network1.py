import networkx as nx
import networkx
import matplotlib.pyplot as plt
import pylab as plt

G = nx.Graph()
G.add_edges_from([('RezaGplzar', 'ElnazShakerdoost',{'weight': 100}), ('RezaGplzar', 'NikiKarimi',{'weight': 200}), ('NikiKarimi', 'ElnazShakerdoost',{'weight': 300}), ('HootanShakiba', 'ElnazShakerdoost',{'weight': 300}), ('HootanShakiba', 'MahnazAfshar',{'weight': 100}),
                 ('BahramRadan', 'NavidMohammadzadeh',{'weight': 100}), ('RezaGplzar', 'MahnazAfshar',{'weight': 400}), ('FreshtehHosseini', 'BahramRadan'  ,{'weight': 100}), ('MahnazAfshar', 'NavidMohammadzadeh',{'weight': 200}), ('FreshtehHosseini', 'AfsanehPakro',{'weight': 100}) ,('BahramRadan', 'AmirAghaii',{'weight': 300}) ,('BahramRadan', 'DibaZAhedi',{'weight': 100}), ])

plt.figure() 
plt.grid(True)

plt.legend(['In-degree', 'Out-degree'])
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title('network of places in Cambridge')
plt.xlim([0, 2*10**2])
plt.close()

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
print("1.View Of network Iranian Actor and Actress")
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