from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set([0])
        queue = deque(rooms[0])
        while queue:
            node = queue.popleft()
            if node not in visit:
                visit.add(node)
                queue.extend(rooms[node])
        return len(visit) == len(rooms)
