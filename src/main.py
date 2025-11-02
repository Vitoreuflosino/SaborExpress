# ==============================
# Projeto: Sabor Express
# Autor: VITOR EUFLOSINO
# Data: 02 Novembro/2025
# Descrição: Algoritmo simples para encontrar rotas e agrupar entregas
# ==============================

import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# ====== PARTE 1: REPRESENTAÇÃO DO GRAFO ======
# Criando um grafo da cidade
G = nx.Graph()

# Adicionando nós (bairros/pontos de entrega)
locais = ["Restaurante", "Bairro A", "Bairro B", "Bairro C", "Bairro D"]
G.add_nodes_from(locais)

# Adicionando conexões (ruas com pesos = distância em km)
G.add_weighted_edges_from([
    ("Restaurante", "Bairro A", 2),
    ("Restaurante", "Bairro C", 4),
    ("Bairro A", "Bairro B", 3),
    ("Bairro A", "Bairro D", 2),
    ("Bairro C", "Bairro D", 3)
])

# Desenhar o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Mapa de Entregas - Sabor Express")
plt.savefig("../docs/grafo.png")
plt.show()

# ====== PARTE 2: ALGORITMO A* ======
print("\n=== Cálculo da melhor rota usando A* ===")
rota = nx.astar_path(G, "Restaurante", "Bairro B", weight='weight')
distancia = nx.path_weight(G, rota, weight='weight')
print("Melhor rota:", " → ".join(rota))
print("Distância total:", distancia, "km")

# ====== PARTE 3: AGRUPAMENTO COM K-MEANS ======
print("\n=== Agrupamento de pontos de entrega (K-Means) ===")
# Coordenadas fictícias dos bairros (latitude, longitude)
coordenadas = np.array([
    [1, 2],   # Restaurante
    [2, 4],   # Bairro A
    [3, 5],   # Bairro B
    [4, 1],   # Bairro C
    [5, 2]    # Bairro D
])

# Agrupando em 2 clusters (ex: 2 entregadores)
kmeans = KMeans(n_clusters=2, random_state=0).fit(coordenadas)
rotulos = kmeans.labels_

for i, local in enumerate(locais):
    print(f"{local} pertence ao grupo {rotulos[i]}")

# Visualizando agrupamento
plt.scatter(coordenadas[:, 0], coordenadas[:, 1], c=rotulos, cmap='cool')
plt.title("Agrupamento de Entregas (K-Means)")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.savefig("../docs/agrupamento.png")
plt.show()
