from collections import defaultdict
import heapq


def networkDelayTime(times, N, K):
    graph = defaultdict(list)
    distance = {}
    nodes = []
    for u, v, w in times:
        graph[u].append((v, w))
    for i in range(1, N+1):
        if i == K:
            distance[i] = 0
        else:
            distance[i] = float('inf')
        heapq.heappush(nodes, [distance[i], i])
    while nodes:
        u = heapq.heappop(nodes)[1]
        for neighbor in graph[u]:
            alt = distance[u] + neighbor[1]
            if alt < distance[neighbor[0]]:
                distance[neighbor[0]] = alt
                for n in nodes:
                    if n[1] == neighbor[0]:
                        n[0] = alt
                        break
                heapq.heapify(nodes)
    output = max(distance.values())
    return output if output < float('inf') else -1


if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2
    print(networkDelayTime(times, N, K))


# Time Complexity: using Heap O(ElogE) (E is the number of edges)
# Space Complexity O(N+E), N=no. of nodes, E=no. of edges
# There are N network nodes, labelled 1 to N.
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
