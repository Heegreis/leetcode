class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        nodes = []
        for item in arr:
            nodes.append(Node(item))
        for i, node in enumerate(nodes):
            if i + arr[i] < len(arr):
                node.neighbors.append(nodes[i + arr[i]])
            if i - arr[i] >= 0:
                node.neighbors.append(nodes[i - arr[i]])
        bfs = BFS(nodes[start])
        
        for node in bfs.traversal():
            if int(node.value()) == 0:
                return True
        return False
    
        
        
class Node:
    
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.neighbors = []
        
    def value(self):
        return self.name
    
class BFS:
    """
    For BFS, use queue; For DFS, use stack or recursion
    """
    def __init__(self, start):
        self.queue = []
        self.start = start
        
    def traversal(self):
        self.start.visited = True
        self.queue.append(self.start)
        
        while self.queue:
            
            node = self.queue.pop(0)
            yield node
            
            for n in node.neighbors:
                if not n.visited:
                    n.visited = True
                    self.queue.append(n)