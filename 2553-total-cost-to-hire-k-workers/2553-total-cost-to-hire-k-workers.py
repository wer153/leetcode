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
        front_heap, mid_heap, back_heap = [], [], []
        total_hiring_cost, i, j = 0, 0, len(costs) - 1
        for _ in range(candidates):
            heappush(front_heap, (costs[i], i))
            heappush(back_heap, (costs[j], j))
            i += 1
            j -= 1

        # print(costs, k, candidates, front_heap, back_heap)
        # print(i, j, total_hiring_cost)
        # print(front_heap, back_heap)
        for _ in range(k):
            front, back = heappop(front_heap), heappop(back_heap)
            # print(front, front_heap)
            # print(back, back_heap)
            # total_hiring_cost += min([front[0], back[0]])
            # popped_index.add(min([front,back]))
            if front == back:
                # print('equal')
                popped_index.add(front)
                push_front_heap()
                push_back_heap()
                total_hiring_cost += front[0]
            if front < back:
                heappush(back_heap, back)
                popped_index.add(front)
                push_front_heap()
                total_hiring_cost += front[0]
            if front > back:
                heappush(front_heap, front)
                popped_index.add(back)
                push_back_heap()
                total_hiring_cost += back[0]
                
            
            # print(i, j, total_hiring_cost)
            # if front_heap[0] == back_heap[0]:
            #     total_hiring_cost += heappop(front_heap)[0]
            #     if i < len(costs):
            #         heappush(front_heap, (costs[i], i))
            #     if 0 <= j:
            #         heappush(back_heap, (costs[j], j))
            #     i += 1
            #     j -= 1
            # elif front_heap[0] < back_heap[0]:
            #     total_hiring_cost += heappop(front_heap)[0]
            #     if i < len(costs):
            #         heappush(front_heap, (costs[i], i))
            #     i += 1
            # elif front_heap[0] > back_heap[0]:
            #     total_hiring_cost += heappop(back_heap)[0]
            #     if 0 <= j:
            #         heappush(back_heap, (costs[j], j))
            #     j -= 1
                
        return total_hiring_cost

    

