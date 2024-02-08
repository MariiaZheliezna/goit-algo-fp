import uuid

import networkx as nx
import matplotlib.pyplot as plt

from collections import deque

class Node:
    def __init__(self, key, color='skyblue'):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def bfs_colour(root: Node, queue, color, colors):
    if root.color == 'skyblue':
        root.color = colors[color]
        color +=1
    
    # Обхід за BFS з використанням рекурсії та черги
    if not queue: # Якщо черга порожня, завершуємо рекурсію
        return color
    node_ = queue.popleft()
    if node_.color == 'skyblue':
        node_.color = colors[color]
        color +=1
    if node_.left:
        queue.extend([node_.left])
    if node_.right:
        queue.extend([node_.right])
    color = bfs_colour(root, queue, color, colors)
    return color

def dfs_color(root: Node, color, colors):
    if root.color == 'skyblue':
        root.color = colors[color]
        color += 1
    if root.left:
        color = dfs_color(root.left, color, colors)
    if root.right:
        color = dfs_color(root.right, color, colors)
    return color


def main():
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(8)

    colors = ['#48144D', '#631B69', '#7B2182', '#9D2AA6', '#AE2FB8', '#CD37D9', '#DE3CEB', '#F241FF', '#F98EFF']

    # Змінюємо кольори вузлів
    bfs_colour(root, deque([root]), 0, colors)

    # Відображення дерева
    draw_tree(root)


    # Створення дерева для DFS
    root2 = Node(0)
    root2.left = Node(4)
    root2.left.left = Node(5)
    root2.left.right = Node(10)
    root2.right = Node(1)
    root2.right.left = Node(3)
    root2.right.right = Node(8)

    # Змінюємо кольори вузлів
    dfs_color(root2, 0, colors)

    # Відображення дерева
    draw_tree(root2)

if __name__ =='__main__':
    main()