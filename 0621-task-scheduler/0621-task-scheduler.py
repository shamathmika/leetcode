class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        """
        For this question, you create a hashmap first of the count of 
        each letter. This will take O(26) ~ O(1) space. Now, it has
        to maintain such that the letter with max count stays at the 
        top. For this we use max heap. Since python does not have max
        heap function, we store everything in negative and use the heapify
        method to create the "max" min heap. 
        Next, we create a queue - this will help us keep a list of items
        waiting for their turn in the CPU. A variable time manages time 
        in one unit. So now we run a loop until all the tasks have been
        served in the CPU.
        We pick the first element in the heap and "process" it. i.e., we
        do time += 1. If the count of the task is -1 (since it is stored
        in negative in the heap), we dont add it to the queue. But if it
        is anything else, we "reduce" (add, since it is in negative) the 
        count by n (the cooldown time since this task cant be processed 
        until then) and add it to queue. If the time is equal to the first
        task in the queue, then heap push it to the heap
        """
        _map = Counter(tasks)
        heap = [-m for m in _map.values()]
        heapq.heapify(heap)

        time = 0
        q = deque() # [(-count, timeWhenItCanBeProcessedAgainAfterBeingIdle)]

        while heap or q:
            time += 1

            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append([count, time + n])
                
            if q and q[0][1] == time: # If the first item in the q is ready to be processed after being idle at this time
                heapq.heappush(heap, q.popleft()[0]) # [0] will give -count

        return time

# TC: O(m)
# SC: O(26) = O(1)