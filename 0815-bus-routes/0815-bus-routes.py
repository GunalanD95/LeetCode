from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        q = deque()
        q.append((source, 0))  # start_node, bus_count

        hmap = defaultdict(list)
        bus_station = defaultdict(set)

        for bus_no, bus in enumerate(routes):
            for bus_stop in bus:
                hmap[bus_stop].append(bus_no)
                bus_station[bus_no].add(bus_stop)

        while q:
            bus_stop, bus_count = q.popleft()

            for bus in hmap[bus_stop]:
                if target in bus_station[bus]:
                    return bus_count + 1

                for new_bus_stop in bus_station[bus]:
                    q.append((new_bus_stop, bus_count + 1))
                bus_station[bus] = set()

        return -1
