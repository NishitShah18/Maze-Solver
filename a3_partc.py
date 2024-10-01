import random
from a2d import Graph
from a3_partb import minimum_spanning_tree


def generate_maze(number_of_rows, number_of_columns):
    walls = []
    for i in range(number_of_rows * number_of_columns):
        if (i + 1) % number_of_columns != 0:
            walls.append((i, i + 1))
        if i + number_of_columns < number_of_rows * number_of_columns:
            walls.append((i, i + number_of_columns))
    
    graph = Graph(number_of_rows * number_of_columns)
    for wall in walls:
        cell_1, cell_2 = wall
        weight = random.randint(1, 50)
        graph.add_edge(cell_1, cell_2, weight)
        graph.add_edge(cell_2, cell_1, weight)

    mst = minimum_spanning_tree(graph)

    walls_to_remove = []
    for edge in mst:
        cell_1, cell_2 = edge
        if cell_1 < cell_2:
            walls_to_remove.append((cell_1, cell_2))
        else:
            walls_to_remove.append((cell_2, cell_1))

    for wall in walls_to_remove:
        walls.remove(wall)

    return walls
