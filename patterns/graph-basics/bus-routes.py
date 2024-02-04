'''
bfs graph
building graph using bus instead of stop
'''
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list) # bus no -> [stop]
        stop_to_bus = defaultdict(set) # stop -> [bus]
        depth = 0
        
        for bus_no, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].add(bus_no)
                graph[bus_no].append(stop)
        
        if source == target:
            return 0
        
        candidates = deque(stop_to_bus[source])   # list of bus no
        visited = stop_to_bus[source].copy()  # visited buses
        
        while candidates:
            depth += 1
            for _ in range(len(candidates)):
                candidate = candidates.popleft()
                if candidate in stop_to_bus[target]:
                    return depth
                for stop in graph[candidate]: # stops in bus station
                    unvisited_bus = stop_to_bus[stop] - visited
                    visited |= unvisited_bus
                    for bus in unvisited_bus:
                        candidates.append(bus)
        else:
            return -1
