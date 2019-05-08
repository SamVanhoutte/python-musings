###############################################
# Sam Vanhoutte - PG Applied AI - Programming
# Unit tests, for the graph algorithms
###############################################

import unittest                     # unit testing ftw
import graph as gr                  # importing the actual graph class

class TestMethods(unittest.TestCase):
    def test_neighbors_normal(self):
        self.validate_neighbors(3, 3, ['02:10', '02:11', '02:01', '01:03', '03:12', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14'])
        self.validate_neighbors(14, 1, ['02:10', '02:11', '02:01', '01:03', '03:12', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14'])

    def test_neighbors_standalone(self):
        self.validate_neighbors(12, 0, ['02:10', '02:11', '02:01', '01:03', '03:04', '04:13', '04:05', '05:06', '05:09', '09:15', '09:07', '05:06', '06:07', '06:00', '01:00', '08:00', '08:14'])


    def validate_neighbors(self, vertex, expected_neighbors, maze_edges):
        maze = gr.Graph()

        # Add vertices for all other nodes till 15
        for i in range(0, 16):
            maze.add_vertex(gr.Vertex(i)) 

        # Add all edge (0 = S - 15 = T)
        for edge in maze_edges:
            maze.add_edge(int(edge.split(':')[0]), int(edge.split(':')[1]))
        neighbors = maze.get_neighbors(vertex)
        self.assertEqual(len(neighbors), expected_neighbors)
