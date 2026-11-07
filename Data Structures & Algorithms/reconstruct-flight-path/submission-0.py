from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for from_i, to_i in sorted(tickets, reverse=True):
            graph[from_i].append(to_i)
        
        route = []
        stack = ["JFK"]

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        return route[::-1]
        