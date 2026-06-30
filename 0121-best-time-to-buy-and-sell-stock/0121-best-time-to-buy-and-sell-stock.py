class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        We pass through the array once. For each element we check if it is lesser than the
        global minimum value we have saved. If so, save it as the global min. At this point
        you can't also be on the maximum price. So its either that the number is less than 
        the global min or we check if the current price minus the global min is greater than
        the global profit. If it is, so far this has been the best combo of min and max values.
        If in a later position the global min changes, the global profit still has the max
        profit so far. So unless in a later part the profit is higher, it stays so. All
        cases work in this scenario
        [1, 2, 3, 4] -> 1
        [4, 3, 2, 1] -> 0
        [1, 1, 1, 1] -> 0
        [1, 3, 2] -> 2
        """
        mi = float("inf")
        maprofit = 0

        for i in range(len(prices)):
            if mi > prices[i]: # can't do mi = min(mi, prices[i]) because we need the if condition here ...
                mi = prices[i]
            elif ((prices[i] - mi) > maprofit): # ... and here
                maprofit = prices[i] - mi
        
        return maprofit
        # TC: O(N), SC: O(1)

        # """
        # WRONG
        # We can use 2 pointers. One from the left side, the other from the right side.
        # Run the loop until they meet. From left keep finding the minimum, and from 
        # """
        # """
        # WRONG
        # I am thinking, run a loop twice. The first time, find the minimum element's position.
        # In the second loop, start from min position + 1 and find the max. Return max - min
        # This doesnt work for the case [2, 4, 1] because min is 1 and we get 0. But ans is 2
        # """
        # mi = prices[0]
        # minpos = 0
        # l = len(prices)
        # for i in range(l):
        #     if mi > prices[i]:
        #         mi = prices[i]
        #         minpos = i
        
        # ma = mi
        # for i in range(minpos+1, l):
        #     ma = max(ma, prices[i])
        
        # return ma - mi
        # # TC : O(N), SC: O(1)