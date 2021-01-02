'''
    Author: Ajay Mahar
    Lang: python3
    Github: https://www.github.com/ajaymahar
    YT: https://www.youtube.com/ajaymaharyt

'''


from queue import Queue


class Graph:
    def __init__(self, nodes, isDirected=False):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self.nodes = nodes
        self.adjList = {}
        self.isDirected = isDirected

        for node in self.nodes:
            self.adjList[node] = []

    def addEdge(self, v, e):
        """TODO: Docstring for addEdge.
        :returns: TODO

        """
        self.adjList[v].append(e)

        if not self.isDirected:
            self.adjList[e].append(v)

    def bfs(self, node):
        """TODO: Docstring for bfs.
        :returns: TODO

        The time complexity of the breadth-first search as
        T: O(|V|+|E|) == O(n + n) == O(n).
        S: O(|V| + 2|E|)--> for undirected graph
        S: O(|V| + |E|) --> for directe graph

        """
        q = Queue()
        visited = {key: False for key in self.nodes}

        q.put(node)
        visited[node] = True

        while not q.empty():
            node = q.get()
            print(node, end=" ")

            for v in self.adjList[node]:
                if not visited[v]:
                    q.put(v)
                    visited[v] = True

    def dfs(self, node, visited=[]):
        """TODO: Docstring for dfs.
        :returns: TODO
        Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
        Space Complexity :O(V).
        Since an extra visited list is needed of size V.
        """
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            for node in self.adjList[node]:
                self.dfs(node, visited)

    def printGraph(self):
        """TODO: Docstring for printGraph.
        :returns: TODO

        """
        for v, e in self.adjList.items():
            print(f"{v} -> {e}")


if __name__ == "__main__":
    '''
    printGraph example
    A-------B
    |      / | \
    |    /   |  \ E
    |  /     |  /
    C-------D  /

    '''
    # Uncomment below code to test printGraph function

    # nodes = ["A", "B", "C", "D", "E"]
    # edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"),
    #          ("C", "D"), ("B", "E"), ("D", "E")]
    # graphObject = Graph(nodes)

    # for v, e in edges:
    #     graphObject.addEdge(v, e)

    # graphObject.printGraph()

    # ---------------------------------------------------
    # Uncomment below code to test BFS function

    # nodes = ["A", "B", "C", "D", "E", "F"]
    # edges = [("A", "B"), ("A", "C"), ("B", "D"),
    #          ("B", "E"), ("C", "F"), ("E", "F")]
    # graphObject = Graph(nodes)

    # for v, e in edges:
    #     graphObject.addEdge(v, e)

    # graphObject.bfs("A")

    # ---------------------------------------------------
    # Uncomment this code to test the DFS function

    # nodes = ["A", "B", "C", "D", "E", "F"]
    # edges = [("A", "B"), ("A", "C"), ("B", "D"),
    #          ("B", "E"), ("C", "F"), ("E", "F")]
    # graphObject = Graph(nodes, True)

    # for v, e in edges:
    #     graphObject.addEdge(v, e)

    # graphObject.dfs("A")
