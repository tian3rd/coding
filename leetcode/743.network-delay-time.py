#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # initialize distance
        distance = {node: float('inf') for node in range(1, n + 1)}

        # BFS
        queue = collections.deque([(k, 0)])
        distance[k] = 0
        while queue:
            node, dist = queue.popleft()
            for nei, w in graph[node]:
                if distance[nei] > dist + w:
                    distance[nei] = dist + w
                    queue.append((nei, dist + w))

        # find the maximum distance
        max_dist = max(distance.values())
        return max_dist if max_dist < float('inf') else -1
        
# @lc code=end

