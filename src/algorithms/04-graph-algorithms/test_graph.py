###############################################
# Sam Vanhoutte - PG Applied AI - Programming
# Unit tests, for the graph algorithms
###############################################

import unittest                     # unit testing ftw
import graph as gr                  # importing the actual graph class
import graphsearch as gs

class TestMethods(unittest.TestCase):
    def test_neighbors_normal(self):
        self.validate_neighbors(3, 3, ['02:10', '02:11', '02:01', '01:03', '03:12', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14'])
        self.validate_neighbors(14, 1, ['02:10', '02:11', '02:01', '01:03', '03:12', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14'])

    def test_neighbors_standalone(self):
        self.validate_neighbors(12, 0, ['02:10', '10:03', '03:04'])

    def test_successful_df_walks(self):
        self.validate_depth_first(0, 15, True, ['02:10', '02:11', '02:01', '01:03', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14'])
        self.validate_depth_first(0, 15, True, ['00:10', '10:05', '05:08', '08:11', '10:15', '11:13'], 3)

    def test_failed_df_walks(self):
        self.validate_depth_first(0, 15, False, ['00:10', '10:05', '05:08', '08:11', '10:14', '11:13', '09:15'])
        self.validate_depth_first(0, 15, False, [])

    def test_successful_bf_walks(self):
        self.validate_breadth_first(0, 15, True, ['02:10', '02:11', '02:01', '01:03', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14'])
        self.validate_breadth_first(0, 15, True, ['00:10', '10:05', '05:08', '08:11', '10:15', '11:13'])

    def test_failed_bf_walks(self):
        self.validate_breadth_first(0, 15, False, ['00:10', '10:05', '05:08', '08:11', '10:14', '11:13', '09:15'])
        self.validate_breadth_first(0, 15, False, [])

    def test_successful_dijkstra_walks_same_weight(self):
        self.validate_dijkstra(0, 15, True, ['1:3:1', '0:1:1', '1:2:1','3:4:1','4:5:1','5:6:1','6:8:1','6:7:1','6:13:1','3:9:1','9:10:1','10:11:1','10:12:1','12:14:1','9:13:1','13:15:1'], 5)
        self.validate_dijkstra(0, 15, True, ['1:3:1', '0:1:1', '1:2:1','3:4:1','4:5:1','5:6:1','6:8:1','6:7:1','6:13:1','3:9:4','9:10:1','10:11:1','10:12:1','12:14:1','9:13:1','13:15:1', '4:15'], 4)

    def test_successful_dijkstra_walks_diff_weight(self):
        self.validate_dijkstra(0, 15, True, ['1:3:1', '0:1:1', '1:2:1','3:4:1','4:5:1','5:6:1','6:8:1','6:7:1','6:13:1','3:9:5','9:10:1','10:11:1','10:12:1','12:14:1','9:13:1','13:15:1'], 7)
        self.validate_dijkstra(0, 15, True, ['1:3:1', '0:1:1', '1:2:1','3:4:1','4:5:1','5:6:1','6:8:1','6:7:1','6:13:1','3:9:4','9:10:1','10:11:1','10:12:1','12:14:1','9:13:1','13:15:1', '4:15:3'], 6)

    def test_failed_dijkstra_walks(self):
        self.validate_dijkstra(0, 15, False, ['00:10', '10:05', '05:08', '08:11', '10:14', '11:13', '09:15'])
        self.validate_dijkstra(0, 15, False, [])

    def create_maze(self, maze_edges):
        maze = gr.Graph()
        # Add vertices for all other nodes till 15
        for i in range(0, 16):
            maze.add_vertex(gr.Vertex(i)) 

        for edge in maze_edges:
            edge_parts = edge.split(':')
            if(len(edge_parts)==3): # definition with distance/weight added
                maze.add_edge(int(edge_parts[0]), int(edge_parts[1]), int(edge_parts[2]))
            else:
                maze.add_edge(int(edge_parts[0]), int(edge_parts[1]))

        return maze

    def validate_depth_first(self, start, target, should_find_path, maze_edges, exact_steps = -1):
        maze = self.create_maze(maze_edges)
        walked_path_vertices = gs.walk_depth_first(maze, start, target)
        self.assertEqual(should_find_path, walked_path_vertices!=None)
        if(exact_steps >= 0):
            self.assertEqual(exact_steps, len(walked_path_vertices))

    def validate_breadth_first(self, start, target, should_find_path, maze_edges, exact_steps = -1):
        maze = self.create_maze(maze_edges)
        walked_path_vertices = gs.walk_breadth_first(maze, start, target)
        self.assertEqual(should_find_path, walked_path_vertices!=None)
        if(exact_steps >= 0):
            self.assertEqual(exact_steps, len(walked_path_vertices))

    def validate_dijkstra(self, start, target, should_find_path, maze_edges, expected_distance = -1):
        maze = self.create_maze(maze_edges)
        total_distance, walked_path_vertices = gs.do_the_dijkstra(maze, start, target)
        self.assertEqual(should_find_path, walked_path_vertices!=None)
        if(expected_distance >= 0):
            self.assertEqual(expected_distance, total_distance)


    def validate_neighbors(self, vertex, expected_neighbors, maze_edges):
        maze = self.create_maze(maze_edges)
        neighbors = maze.get_neighbors(vertex)
        for n in neighbors:
            print('neighbor found')
            n.print()
        self.assertEqual(len(neighbors), expected_neighbors)
