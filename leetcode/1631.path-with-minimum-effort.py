#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # need to import queue to use PriorityQueue
        import queue, collections

        num_rows, num_cols = len( heights ), len(heights[0])
        graph = collections.defaultdict(list)
        dist_to = collections.defaultdict()

        # build graph
        for i in range(num_rows):
            for j in range(num_cols):
                if i > 0:
                    graph[(i, j)].append(((i - 1, j), abs(heights[i][j] - heights[i - 1][j])))
                if i < num_rows - 1:
                    graph[(i, j)].append(((i + 1, j), abs(heights[i][j] - heights[i + 1][j])))
                if j > 0:
                    graph[(i, j)].append(((i, j - 1), abs(heights[i][j] - heights[i][j - 1])))
                if j < num_cols - 1:
                    graph[(i, j)].append(((i, j + 1), abs(heights[i][j] - heights[i][j + 1])))
                dist_to[(i, j)] = float('inf')
        dist_to[(0, 0)] = 0

        # dijkstra
        def dijkstra(start, end, graph):
            pq = queue.PriorityQueue()
            pq.put((0, start))
            while not pq.empty():
                dist, cur_node = pq.get()
                if (cur_node == end):
                    return dist
                for next_node, next_dist in graph[cur_node]:
                    # only care about absolute difference rather than accumulated differences
                    if dist_to[next_node] > max(dist, next_dist):
                        dist_to[next_node] = max(dist, next_dist)
                        pq.put((dist_to[next_node], next_node))
        
        effort = dijkstra((0, 0), (num_rows - 1, num_cols - 1), graph)
        return effort if effort != float('inf') else -1

# @lc code=end

