graph={
    'A':['B','C'],
    'B':[],
    'C':["D","E"],
    'D':["H"],
    'E':["F"],
    'H':["I"],
    'F':["G"],
    'I':["J"],
    'J':[],
    'G':[]
    
}
def bfs(visited,grah,current_node):
    visited.append(current_node)
    queue = []
    queue.append(current_node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs([],graph,'A')
            
