class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Calculate time taken for each car to reach the target
        time_taken = [(target - pos) / spd for pos, spd in zip(position, speed)]
        
        # Pair positions with their corresponding times and sort by position in descending order
        paired = sorted(zip(position, time_taken), key=lambda x: -x[0])
        
        fleets = 0
        last_time = 0
        
        # Iterate through the sorted list to determine the number of fleets
        for pos, time in paired:
            if time > last_time:  # New fleet is formed
                fleets += 1
                last_time = time  # Update the last time
        
        return fleets
