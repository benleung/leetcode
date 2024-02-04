'''
speed not enough
'''
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        visited_by_node1 = defaultdict(lambda: -1)  # index -> distance
        visited_by_node2 = defaultdict(lambda: -1)  # index -> distance
        
        distance = 0
        stack = [node1]
        while stack:
            to_visit = stack.pop()
            visited_by_node1[to_visit] = distance
            
            visit_next = edges[to_visit]
            if visit_next != -1 and visited_by_node1[visit_next] == -1:  # not already visited, not no outgoing
                stack.append(visit_next)
                distance += 1
        # print(visited_by_node1) # {0: 0, 1: 1, 2: 2}
        
        
        
        distance = 0
        stack = [node2]
        while stack:
            to_visit = stack.pop()
            visited_by_node2[to_visit] = distance
            
            visit_next = edges[to_visit]
            if visit_next != -1 and visited_by_node2[visit_next] == -1:  # not already visited, not no outgoing
                stack.append(visit_next)
                distance += 1
        
        # print(visited_by_node2) # {2: 0}
        
        target_distance = inf
        for i in range(len(edges)):
            if visited_by_node1[i] == -1 or visited_by_node2[i] == -1:
                continue
            
            dist = max(visited_by_node1[i], visited_by_node2[i])

            target_distance = min(target_distance, dist)
            
            
        for i in range(len(edges)):
            if visited_by_node1[i] == -1 or visited_by_node2[i] == -1:
                continue
            
            if max(visited_by_node1[i], visited_by_node2[i]) == target_distance:
                return i
        
        return -1
