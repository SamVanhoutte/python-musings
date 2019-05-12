import graph as gr

def track_walk_back(path_vertices, start_vertex, target_vertex):
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
                print('Target vertex reached !!!')
                # now return a list of all visited items on the path (and remove the closed ones)
                return track_walk_back(path_vertices, start_vertex_id, target_vertex_id)

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
                print('Target vertex reached !!!')
                # now return a list of all visited items on the path (and remove the closed ones)
                return track_walk_back(path_vertices, start_vertex_id, target_vertex_id)

    # When we arrive here, no valid path was found
    return None

def do_the_dijkstra(maze, start_vertex_id, target_vertex_id, max_depth = 5):
    inf = float('inf')
    distances = {vertex: inf for vertex in maze.vertices}
    previous_vertices = {
        vertex: None for vertex in maze.vertices
    }
    distances[start_vertex_id] = 0
    vertices_to_process = maze.vertices.copy()

    while vertices_to_process:
        # Taking the smallest (least distance) vertex from the list
        current_vertex = min(
            vertices_to_process, key=lambda vertex: distances[vertex])
        # vertices_to_process.remove(current_vertex)
        del(vertices_to_process[current_vertex])
        if distances[current_vertex] == inf:
            #todo : why ?
            break
        for neighbor in maze.get_neighbors(current_vertex):
            neighbor_distance = maze.edges[current_vertex][neighbor.name]
            alternative_route = distances[current_vertex] + neighbor_distance
            if alternative_route < distances[neighbor.name]:
                distances[neighbor.name] = alternative_route
                previous_vertices[neighbor.name] = current_vertex

    # path, current_vertex = deque(), dest
    current_vertex = target_vertex_id
    path=None
    while previous_vertices[current_vertex] is not None:
        if(path==None): path = []
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    if path:
        path.append(current_vertex)
        return distances[target_vertex_id], list(reversed(path))
    else:
        return -1, None

def main():
    maze = gr.Graph()
    # Add vertices for all other nodes till 15
    for i in range(0, 16):
        maze.add_vertex(gr.Vertex(i)) 

    #for edge in ['02:10', '02:11', '02:01', '01:03', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14']:
    for edge in ['1:3:1', '0:1:1', '1:2:1','3:4:1','4:5:1','5:6:1','6:8:1','6:7:1','6:13:1','3:9:4','9:10:1','10:11:1','10:12:1','12:14:1','9:13:1','13:15:1']:
        edge_parts = edge.split(':')
        if(len(edge_parts)==3):
            maze.add_edge(int(edge_parts[0]), int(edge_parts[1]), int(edge_parts[2]))
        else:
            maze.add_edge(int(edge_parts[0]), int(edge_parts[1]))
    total_distance, path = do_the_dijkstra(maze, 00, 15)
    print('Total distance:', total_distance)
    print(path)
    # display some lines


if __name__ == "__main__": main()