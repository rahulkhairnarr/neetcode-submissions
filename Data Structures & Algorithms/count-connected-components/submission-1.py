class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        queue = []
        visited = set()

        adj_list = [[] for _ in range(n)]

        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        def bfs():
            while queue:
                node = queue.pop(0)

                for n in adj_list[node]:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
        counts = 0
        for i in range(n):
            if i not in visited:
                counts += 1
                queue.append(i)
                visited.add(i)
                bfs()


        return counts
                


