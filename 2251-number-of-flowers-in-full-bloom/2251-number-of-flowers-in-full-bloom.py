class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        events = []
        OPEN, CLOSE = 1, -1
        for s, e in flowers:
            events.append((s, OPEN))
            events.append((e + 1, CLOSE))
        events.sort()
        
        event_index = 0
        flowers = 0
        answer = [0] * len(persons)
        persons = sorted([(time, index) for index, time in enumerate(persons)])
        for time, person_index in persons:
            while event_index < len(events) and events[event_index][0] <= time:
                flowers += events[event_index][1]
                event_index += 1
            answer[person_index] = flowers
        return answer        