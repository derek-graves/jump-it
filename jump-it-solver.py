from collections import defaultdict

#Find shortest path in a Jump-It board, assuming given board is a DAG (which is true of all Jump-It boards)

class JumpIt:
  def __init__(self,board):

    #board must start with a 0
    if board[0] != 0:
      board.insert(0,0)

    self.vertices = len(board)
    self.board = board
    self.graph = defaultdict(list)

    #update self.graph to contain the adjacency list for each vertex.
    #since the only valid moves are proceeding or skipping 1 cell,
    #the adjacency list for each vertex contains at most 2 other vertices
    for index in range(self.vertices - 1):
      self.graph[index].append((index + 1, board[index + 1]))
      if index < len(board) - 2:
        self.graph[index].append((index + 2, board[index + 2]))

  #assumes self.graph is topologically ordered
  def minimal_routes(self, source, last = False):
    topo_ordering = []

    #add vertices to topo_ordering in assumed topological order
    for v in self.graph:
      topo_ordering.append(v)

    #initialize all distances (except from the source to itself) to inf
    distances = [float("Inf")] * self.vertices
    distances[source] = 0

    #in topological order, relax all edges
    while topo_ordering:
      current = topo_ordering.pop(0)
      for vertex, weight in self.graph[current]:
        if distances[vertex] > distances[current] + weight:
          distances[vertex] = distances[current] + weight

    #print the minimum distance to the last vertex
    if last:
      print(f"Minimum path for {self.board} is: {distances[-1]}")
    #print minimum distance to each vertex
    else:
      print(distances)

#example
g = JumpIt([1,2,3,4,5])
g.minimal_routes(0, True)
