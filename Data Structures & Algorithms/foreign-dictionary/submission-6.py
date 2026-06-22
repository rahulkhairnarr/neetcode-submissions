from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_dict = defaultdict(set)

        indegree = defaultdict(int)

        for word in words:
            for c in word:
                adj_dict[c] = set()
                indegree[c] = 0

        for i in range(1, len(words)):
            wi = 0
            min_wi = min(len(words[i]), len(words[i-1]))
            while wi < min_wi:
                if words[i-1][wi] != words[i][wi]:
                    if words[i][wi] not in adj_dict[words[i-1][wi]]:
                        adj_dict[words[i-1][wi]].add(words[i][wi])
                        indegree[words[i][wi]] += 1
                    break
                wi +=1
            if wi == min_wi and len(words[i-1]) > len(words[i]):
                return ""

        queue = deque([])
        result = ''

        for k,v in indegree.items():
            if v == 0:
                queue.append(k)

        while queue:
            key = queue.popleft()

            result += key
            for c in adj_dict[key]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)

        if len(result) == len(indegree):
            return result
        
        return ""







