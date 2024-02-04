'''
got stuck in thinking
'''
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # Return the latest time you may arrive at the bus station to catch a bus
        buses.sort()
        passengers.sort()
        
        passengers_set = set()
        
        B = len(buses)
        P = len(passengers)
        
        bus_ptr = 0
        passenger_ptr = 0
        
        h = defaultdict(set)  # bus -> set(...) (list of passengers)
        
        while bus_ptr < B and passenger_ptr < P:
            bus = buses[bus_ptr]
            passenger = passengers[passenger_ptr]
            
            if passenger > bus:
                bus_ptr += 1
                continue
            
            h[bus].add(passenger)
            passengers_set.add(passenger)
            
            if len(h[bus]) == capacity:
                bus_ptr += 1
            
            passenger_ptr += 1
        
        # print(h)
        
        # for i in range(B-1, -1, -1):
        bus = buses[B-1]
        if len(h[bus]) < capacity:
            candidate = bus
            while True:
                # should insert in this bus
                if candidate not in passengers_set:
                    return candidate
                else:
                    candidate -= 1
        else:
            candidate = max(passengers_set)
            while True:
                candidate -= 1
                if candidate not in passengers_set:
                    return candidate

        
        
                
        
        
                