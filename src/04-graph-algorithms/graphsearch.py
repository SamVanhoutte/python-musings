import graph as gr

# Solve maze using Pre-Order DFS algorithm, terminate with solution
def walk_depth_first(maze, start_vertex_id, target_vertex_id, max_depth = 5):
    start_vertex = gr.Vertex(start_vertex_id)
    target_vertex = gr.Vertex(target_vertex_id)

    if start_vertex == target_vertex:
        print('The target and start were equal.  Returning empty list')
        return []
    
    #Start with first vertex and add it to the stack
    current_options_stack = [start_vertex]
    path_vertices = {}

    while current_options_stack:
        # take next vertex from the options stack
        current_vertex = current_options_stack.pop()
        # indicate the state on the vertex as Work in progress
        current_vertex.state = gr.VertexState.Wip
        # get neighboring vertices that are not yet closed as dead end
        possible_next_steps = maze.get_neighbors(current_vertex.name)
        
        # if no more neighbors are found (except the previous edge), close the vertex
        if len(possible_next_steps) <= 1 and current_vertex.name != start_vertex_id:
            current_vertex.state = gr.VertexState.Closed
        
        # if we have already investigated this vertex, skip this loop and move to the next
        if current_vertex.name in path_vertices.keys():
            continue
        
        path_vertices[current_vertex.name] = current_vertex
        
        # add the next possible steps to the stack
        for possible_step in possible_next_steps:
            current_options_stack.append(possible_step)
            # when target is part of the next steps, add the last vertex to the path and exit the loop
            if possible_step.name == target_vertex.name:
                path_vertices[target_vertex.name] = target_vertex
                print('Target vector reached !!!')
                # now return a list of all visited items on the path (and remove the closed ones)
                return [v for v in path_vertices.values() if v.state != gr.VertexState.Closed]

    # When we arrive here, no valid path was found
    return None
    
def generate_maze(dimensions = 8):
    maze = gr.Graph()

    # Add vertices for all other (numeric) nodes
    for i in range(0, 16):
        maze.add_vertex(gr.Vertex(i)) #f"{i:02d}"))

    # Add all edge (0 = S - 15 = T)
    edges = ['02:10', '02:11', '02:01', '01:03', '03:12', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14']
    edges = ['02:10', '02:11', '02:01', '01:03', '03:12', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '08:07', '08:00', '08:14']
    for edge in edges:
        maze.add_edge(int(edge.split(':')[0]), int(edge.split(':')[1]))
    return maze

#maze = generate_maze()
#maze.print_graph()
#for n in maze.get_neighbors(3):
#    n.print()
#walked_path_vertices = walk_depth_first(maze, 0, 15)
#for path_vertex in walked_path_vertices:
#    path_vertex.print()
#print(walked_path_vertices)