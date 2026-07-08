# Number of Provinces LC 547

isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

"""
it is same as Num of islands problem but here we have adjacency list,not 2d matrix

      1 2 3

1 ->  1 1 0

2 ->  1 1 0

3 ->  0 0 1
1 is connected to 1 
1 is connected to 2
1 is not connected to 3
like thiss

so main difference is dirs 
"""

def findCircleNum(isConnected):
    n=len(isConnected)
    visited=[False]*n 
    provinces=0

    def dfs(city):
        visited[city]=True 

        for neighbour in range(n):
            if isConnected[city][neighbour]==1 and not visited[neighbour]:
                dfs(neighbour)
    
    for city in range(n):
        if not visited[city]:
            dfs(city)
            provinces+=1
    return provinces

print(findCircleNum(isConnected))


"""
| Problem             | Representation           | DFS Parameter | Neighbor Finding        |
| ------------------- | ------------------------ | ------------- | ----------------------- |
| Number of Islands   | Grid                     | `dfs(r, c)`   | Up, Down, Left, Right   |
| Max Area of Island  | Grid                     | `dfs(r, c)`   | Up, Down, Left, Right   |
| Max Fish            | Grid                     | `dfs(r, c)`   | Up, Down, Left, Right   |
| Number of Provinces | Graph (Adjacency Matrix) | `dfs(city)`   | Loop through all cities |


For Number of Provinces, neighbors are defined by the adjacency matrix:

for neighbour in range(n):
    if isConnected[city][neighbour] == 1 and not visited[neighbour]:
        dfs(neighbour)
"""
