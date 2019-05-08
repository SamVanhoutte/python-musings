import graph as gr

def track_back(path_vertices, start_vertex, target_vertex):
    path = [target_vertex]
    current_step = target_vertex
    while current_step != start_vertex:
        print(current_step, path_vertices[current_step])
        path.insert(0, path_vertices[current_step].name)
        current_step = path_vertices[current_step].name
    return path

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
    previous_vertex = start_vertex

    while current_options_stack:
        # take next vertex from the options stack
        current_vertex = current_options_stack.pop()
        # indicate the state on the vertex as Work in progress
        # get neighboring vertices that are not yet closed as dead end
        possible_next_steps = maze.get_neighbors(current_vertex.name)
        
        # if no more neighbors are found (except the previous edge), close the vertex
        if len(possible_next_steps) <= 1 and current_vertex.name != start_vertex_id:
            current_vertex.state = gr.VertexState.Closed
            continue
        
        # if we have already investigated this vertex, skip this loop and move to the next
        if current_vertex.name in path_vertices.keys():
            continue
        
        path_vertices[current_vertex.name] = previous_vertex
        previous_vertex = current_vertex
        
        # add the next possible steps to the stack
        for possible_step in possible_next_steps:
            current_options_stack.append(possible_step)
            # when target is part of the next steps, add the last vertex to the path and exit the loop
            if possible_step.name == target_vertex.name:
                path_vertices[target_vertex.name] = previous_vertex
                print('Target vector reached !!!')
                # now return a list of all visited items on the path (and remove the closed ones)
                #return [v for v in path_vertices.values() if v.state != gr.VertexState.Closed]
                return track_back(path_vertices, start_vertex_id, target_vertex_id)

    # When we arrive here, no valid path was found
    return None

def walk_breadth_first(maze, start_vertex_id, target_vertex_id, max_depth = 5):
    start_vertex = gr.Vertex(start_vertex_id)
    target_vertex = gr.Vertex(target_vertex_id)

    if start_vertex == target_vertex:
        print('The target and start were equal.  Returning empty list')
        return []
    
    #Start with first vertex and add it to the stack
    current_options_queue = [start_vertex]
    path_vertices = {}
    previous_vertex = start_vertex

    while current_options_queue:
        # take next vertex from the options stack
        current_vertex = current_options_queue[0]
        current_options_queue.remove(current_options_queue[0])
        # indicate the state on the vertex as Work in progress
        # get neighboring vertices that are not yet closed as dead end
        possible_next_steps = maze.get_neighbors(current_vertex.name)
        
        # if no more neighbors are found (except the previous edge), close the vertex
        if len(possible_next_steps) <= 1 and current_vertex.name != start_vertex_id:
            current_vertex.state = gr.VertexState.Closed
            continue
        
        # if we have already investigated this vertex, skip this loop and move to the next
        if current_vertex.name in path_vertices.keys():
            continue
        
        path_vertices[current_vertex.name] = previous_vertex
        previous_vertex = current_vertex
        
        # add the next possible steps to the stack
        for possible_step in possible_next_steps:
            current_options_queue.append(possible_step)
            # when target is part of the next steps, add the last vertex to the path and exit the loop
            if possible_step.name == target_vertex.name:
                path_vertices[target_vertex.name] = previous_vertex
                print('Target vector reached !!!')
                # now return a list of all visited items on the path (and remove the closed ones)
                #return [v for v in path_vertices.values() if v.state != gr.VertexState.Closed]
                return track_back(path_vertices, start_vertex_id, target_vertex_id)

    # When we arrive here, no valid path was found
    return None
   