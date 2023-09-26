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

        i, j = candidates, len(costs) - 1 - candidates
        front_heap = [(costs[index], index) for index in range(i)]
        back_heap = [(costs[index], index) for index in range(len(costs)-1, j, -1)]
        heapify(front_heap), heapify(back_heap)
        total_hiring_cost, popped_index = 0, set()

        for _ in range(k):
            front, back = front_heap[0], back_heap[0]
            smaller = front if front <= back else back
            popped_index.add(smaller)
            total_hiring_cost += smaller[0]
            if front <= back:
                heappop(front_heap)
                push_front_heap()
            if front >= back:
                heappop(back_heap)
                push_back_heap()
                
        return total_hiring_cost

    

