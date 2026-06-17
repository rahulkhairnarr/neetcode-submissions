class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        queue = []

        adj_list = [[] for _ in range(n)]
        visited = set()
        
        count = 0

        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        def is_connected():
            nonlocal queue
            while queue:
                node, parent = queue.pop(0)

                for n in adj_list[node]:
                    if n not in visited:
                        queue.append((n,node))
                        visited.add(n)
                    elif n in visited and n != parent:
                        return False


        for i in range(n):
            if i not in visited:
                queue.append((i,None))
                visited.add(i)
                count +=1
                if count > 1:
                    return False
                connect = is_connected()
                if not connect and connect is not None:
                    return False
        
        return True


        