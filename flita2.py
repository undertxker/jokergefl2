import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Чтение матрицы из файла
with open('matrix.txt', 'r') as f:
    matrix = []
    for line in f:
        matrix.append([int(x) for x in line.split()])

#Создание графа из матрицы смежности
graph = nx.from_numpy_array(np.array(matrix), create_using=nx.Graph)

#Вычисление позиций вершин для отображения графа
pos = nx.spring_layout(graph)

#Отрисовка графа с помощью Matplotlib
nx.draw(graph, pos)
labels = {i: i for i in range(len(graph.nodes))}
# Установка размера фигуры
nx.draw(graph, pos, with_labels=True, node_size=500, font_size=10, font_weight='bold')
plt.show()
