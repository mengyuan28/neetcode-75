class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       cars = list(zip(position, speed))
       cars.sort(key = lambda x: x[0], reverse=True)
       fleet: List[float] = []
       for pos, spd in cars:
           arrival = (target - pos) / spd
           if not fleet or arrival > fleet[-1]:
               fleet.append(arrival)
        
       return len(fleet)