import sys
import random
import graph as gr

# Solve maze using Pre-Order DFS algorithm, terminate with solution
def walk_depth_first(maze, start_vertex, target_vertex, max_depth = 5):
    if start_vertex == target_vertex:
        return ""
    depth = 0
    current_options_stack = [start_vertex]
    path_vertices = []
    while current_options_stack:
        # take next vertex from the options stack
        current_vertex = current_options_stack.pop()
        if current_vertex in path_vertices:
            # if we have already investigated this vertex, skip this loop and move to the next
            continue
        path_vertices.append(current_vertex)
        for possible_step in maze.get_neighbors(current_vertex):
            print(possible_step)
            current_options_stack.append(possible_step)

def generate_maze(dimensions = 8):
    maze = gr.Graph()

    # Add vertices for all other (numeric) nodes
    for i in range(0, 16):
        maze.add_vertex(gr.Vertex(i)) #f"{i:02d}"))

    # Add all edge (0 = S - 15 = T)
    edges = ['02:10', '02:11', '02:01', '01:03', '03:12', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14']
    for edge in edges:
        maze.add_edge(int(edge.split(':')[0]), int(edge.split(':')[1]))
    return maze

maze = generate_maze()
maze.print_graph()
print(maze.get_neighbors(3))
walk_depth_first(maze, 0, 15)