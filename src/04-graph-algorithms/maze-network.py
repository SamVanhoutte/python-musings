import sys
import random
import graph as gr

# Solve maze using Pre-Order DFS algorithm, terminate with solution
def walk_depth_first(vertex_names, maze):
    stack = []
    current_cell = 0

    while current_cell != maze.total_cells -1:
        print(current_cell)
        cells_to_visit = maze.cell_neighbors(current_cell)
        if len(cells_to_visit) >= 1:
            # choose random neighbor to be new cell
            new_cell_index = random.randint(0, len(cells_to_visit) - 1)
            new_cell, compass_index = cells_to_visit[new_cell_index]
            # knock down wall between it and current cell using visited_cell
            maze.visit_cell(current_cell, new_cell, compass_index)
            # push current cell to stack
            stack.append(current_cell)
            # set current cell to new cell
            current_cell = new_cell
            # add 1 to visited cells
        else:
            maze.backtrack(current_cell)
            current_cell = stack.pop()
            print("run")
        maze.refresh_maze_view()
    maze.state = 'idle'

def generate_maze(dimensions = 8):
    maze = gr.Graph()

    maze.add_vertex(gr.Vertex('SS'))
    maze.add_vertex(gr.Vertex('TT'))
    # Add vertices for all other (numeric) nodes
    for i in range(1, 15):
        maze.add_vertex(gr.Vertex(f"{i:02d}"))

    # Add all edge (0 = S - 15 = T)
    edges = ['02:10', '02:11', '02:01', '01:03', '03:12', '03:04', '04:13', '04:05', '05:06', '05:09', '09:TT', '09:07', '05:06', '06:07', '06:SS', '01:SS', '08:SS', '08:14']
    for edge in edges:
        # print(edge.split(':')[0], edge.split(':')[1])
        maze.add_edge(edge.split(':')[0], edge.split(':')[1])
    return maze

maze = generate_maze()
maze.print_graph()
