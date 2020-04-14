"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2.
        """
        # Check if the vertices exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR: Could not add edge, vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        BREADTH FIRST USES QUEUE
        """
      
        qq = Queue()
        qq.enqueue([starting_vertex])
        visited = list()
        while qq.size() > 0:
            path = qq.dequeue()
            if path[-1] not in visited:
                visited.append(path[-1]) 
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
                    
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        DEPTH FIRST USES STACK
        """
        st = Stack()
        st.push([starting_vertex])
        visited = list()
        while st.size() > 0:
            path = st.pop()
            if path[-1] not in visited:
                visited.append(path[-1])
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    st.push(new_path)
    
        return visited
                #     if self.get_neighbors(starting_vertex):
                #     for next_vert in self.get_neighbors(path[-1]):
                #         new_path = list(path)
                #         new_path.append(next_vert)
                #         st.push(new_path)
                # else: 
                #     return starting_vertex

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
               
    
    def bfs(self, starting_vertex, destination_vertex):
        qt = Queue()
        qt.enqueue([starting_vertex])
        visited = set()
        while qt.size() > 0:
            path = qt.dequeue()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for neighborino in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(neighborino)
                    qt.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        st = Stack()
        st.push([starting_vertex])
        visited = set()
        while st.size() > 0:
            path = st.pop()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for neighborino in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(neighborino)
                    st.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        if path is None:
            path = list()
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path = path + [starting_vertex]
            if starting_vertex == destination_vertex:
                return path
            for neighborino in self.get_neighbors(starting_vertex):
                cat = self.dfs_recursive(neighborino, destination_vertex, path, visited)
                if cat:
                    return cat

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    # '''
    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     # 1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    graph.dft(1)
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

