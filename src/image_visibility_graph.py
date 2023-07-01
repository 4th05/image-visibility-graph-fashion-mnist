import numpy as np
import networkx as nx

#Athor: Athos M. Moraes
#Reference: https://github.com/Jaia89/Image_Visibility

def image_visibility_graph(I, criterion, lattice):
    n_rows, n_columns = I.shape

    if n_rows != n_columns:
        raise ValueError("Input image must be square")

    if criterion not in ['horizontal', 'natural']:
        raise ValueError("Criterion string must be 'natural' or 'horizontal'")

    if not isinstance(lattice, bool):
        raise ValueError("lattice must be bool: True to save lattice structure, False otherwise")

    I = I.astype(float)
    G = nx.Graph()

    if criterion == 'horizontal':
        for i in range(n_rows):
            for j in range(n_columns):
                node_id = i * n_columns + j

                if not lattice:
                    lattice_connections = [(0, 1), (1, 1), (1, 0), (1, -1)]
                    for di, dj in lattice_connections:
                        if 0 <= i + di < n_rows and 0 <= j + dj < n_columns:
                            G.add_edge(node_id, (i + di) * n_columns + (j + dj))

                for c in range(j + 2, n_columns):
                    cond = True
                    for l in range(j + 1, c):
                        if I[i, l] >= I[i, j] or I[i, l] >= I[i, c]:
                            cond = False
                            break
                    if cond:
                        G.add_edge(node_id, i * n_columns + c)

                if i < n_rows - 1:
                    for r in range(i + 2, n_rows):
                        cond = True
                        for l in range(i + 1, r):
                            if I[l, j] >= I[i, j] or I[l, j] >= I[r, j]:
                                cond = False
                                break
                        if cond:
                            G.add_edge(node_id, r * n_columns + j)
    elif criterion == 'natural':
        for i in range(n_rows):
            for j in range(n_columns):
                node_id = i * n_columns + j

                if not lattice:
                    lattice_connections = [(0, 1), (1, 1), (1, 0), (1, -1)]
                    for di, dj in lattice_connections:
                        if 0 <= i + di < n_rows and 0 <= j + dj < n_columns:
                            G.add_edge(node_id, (i + di) * n_columns + (j + dj))

                for c in range(j + 2, n_columns):
                    cond = True
                    for l in range(j + 1, c):
                        if I[i, l] >= I[i, j] + (I[i, c] - I[i, j]) * (l - j) / (c - j):
                            cond = False
                            break
                    if cond:
                        G.add_edge(node_id, i * n_columns + c)

                for r in range(i + 2, n_rows):
                    cond = True
                    for l in range(i + 1, r):
                        if I[l, j] >= I[i, j] + (I[r, j] - I[i, j]) * (l - i) / (r - i):
                            cond = False
                            break
                    if cond:
                        G.add_edge(node_id, r * n_columns + j)
                        
    for node_id in G.nodes():
        i, j = divmod(node_id, n_columns)
        G.nodes[node_id]['coords'] = (i, j)
        G.nodes[node_id]['value'] = I[i, j]

    return G