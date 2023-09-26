from heapq import heapify, heappush
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        def push_front_heap():
            nonlocal i
            while i < len(costs):
                node = (costs[i], i)
                if node not in popped_index:
                    heappush(front_heap, node)
                    i += 1
                    break
                i += 1
            
        def push_back_heap():
            nonlocal j
            while 0 <= j:
                node = (costs[j], j)
                if node not in popped_index:
                    heappush(back_heap, node)
                    j -= 1
                    break
                j -= 1

        popped_index = set()
        front_heap, back_heap = [], []
        total_hiring_cost, i, j = 0, 0, len(costs) - 1
        for _ in range(candidates):
            heappush(front_heap, (costs[i], i))
            heappush(back_heap, (costs[j], j))
            i += 1
            j -= 1

        for _ in range(k):
            front, back = heappop(front_heap), heappop(back_heap)
            smaller = front if front <= back else back
            popped_index.add(smaller)
            total_hiring_cost += smaller[0]
            if front == back:
                push_front_heap()
                push_back_heap()
            if front < back:
                heappush(back_heap, back)
                push_front_heap()
            if front > back:
                heappush(front_heap, front)
                push_back_heap()
                
        return total_hiring_cost

    

