import heapq


def min_meeting_room(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    free_room = []
    heapq.heappush(free_room, intervals[0][1])
    for interval in intervals[1:]:
        if free_room[0] <= interval[0]:
            heapq.heappush(free_room)
        heapq.heappush(free_room, interval[1])
    return len(free_room)


if __name__ == "__main__":
    intervals = [[6, 15], [13, 20], [6, 17]]
    print(min_meeting_room(intervals))


# Time Complexity O(NlogN)
# Space Complexity O(N)
