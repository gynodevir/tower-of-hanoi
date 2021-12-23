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
def bfs(visited,graph,current):
    visited.append(current)
    queue=[]
    queue.append(current)
    while queue:
        s=queue.pop(0)
        print(s,end=' ')
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
while True:

    print("\nenter 1 to do bfs")
    print("enter 2 to exit")
    ch=int(input())
    if ch==1:
        bfs([],graph,'A')
    else:
        break
    
        
        
