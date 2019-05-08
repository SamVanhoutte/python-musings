import numpy as np
from enum import Enum

class VertexState(Enum):
	Open = 0
	Wip = 1
	Closed = -1

class Vertex:
	def __init__(self, n):
		self.name = n
		self.state = VertexState.Open

	def print(self):
			print('Vertex', self.name, ':', self.state)

class Graph:
	# def __init__(self, n):
	vertices = {}
	edges = []
	edge_indices = {}
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			for edge in self.edges:
				edge.append(0)
			self.edges.append([0] * (len(self.edges)+1))
			self.edge_indices[vertex.name] = len(self.edge_indices)
			return True
		else:
			print('vertex', vertex.name, 'not added')
			return False
	
	def add_edge(self, u, v, weight=1):
		if u in self.vertices and v in self.vertices:
			self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
			self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
			return True
		else:
			print('could not add edge', u, v)
			return False
	
	def get_neighbors(self, vertex_name):
		if vertex_name in self.vertices:
			vertex_edges = np.array(list(self.edges[self.edge_indices[vertex_name]]))
			edge_array = np.array(list(self.vertices.keys()))
			neighboring_vertices = [self.vertices.get(key) for key in list(edge_array[vertex_edges > 0])]
			return [v for v in neighboring_vertices if v.state != VertexState.Closed and v.name != vertex_name]

	def print_graph(self):
		for v, i in sorted(self.edge_indices.items()):
			print(str(v) + ' ', end='')
			for j in range(len(self.edges)):
				print(self.edges[i][j], end='')
			print(' ')	

	def print_status(self):
		for vertex in self.vertices.values():
    			vertex.print()
			