graph = {
  '1' : ['2','3'],
  '2' : ['4', '5', '6'],
  '4' : [],
  '5' : ['7'],
  '7' : [],
  '6' : [],
  '3' : ['8', '9'],
  '8' : ['10'],
  '10' : [],
  '9' : []
  }
 
visitedDFS = [] #To store the visited nodes in DFS
visitedBFS = [] #To store the visited nodes in BFS

def dfs(graph, visitedDFS, node): #Recursive function to calculate DFS
    if notInVisited(node, visitedDFS) == False: #if node is not present in visited list then:
        visitedDFS.append(node) #appending the node to the visited list
        for i in graph[node]: #this loop with call the DFS function for the current node which will give the next node in DFS
            dfs(graph, visitedDFS, i)
       
       
def notInVisited(node, visited): #this function takes a node and visited list and checks if the node is already visited
    for i in range(len(visited)):
        if node == visited[i]:
            return True
    return False
   
def bfs(graph, visitedBFS, node):
    if notInVisited(node, visitedBFS) == False:
        visitedBFS.append(node)
        for i in graph:
            for j in graph[i]:
                bfs(graph, visitedBFS, j)
 
def display(visited, graph): #this function will just displays the tree/graph and the result of the search algorithm
    print("Nodes :: Adjacent Nodes")
    for key in graph:
        print(key," -> ", graph[key])
    print(visited)
   
dfs(graph, visitedDFS, '1')
display(visitedDFS, graph)
print("--------------------------------------------------")
bfs(graph, visitedBFS, '1')
display(visitedBFS, graph)