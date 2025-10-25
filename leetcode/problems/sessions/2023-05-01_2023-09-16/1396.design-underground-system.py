#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start

# * Design and Hash Table Solution | O(1) Time | O(n) Space
# * n -> The number of customers and (start station, end station) map


class CustomerCheckInData:
    def __init__(self, start_station: str = "", start_time: int = 0) -> None:
        self.start_station = start_station
        self.start_time = start_time


class StationData:
    def __init__(self, total_travel_time: int = 0, count: int = 0) -> None:
        self.total_travel_time = total_travel_time
        self.count = count


class UndergroundSystem:
    def __init__(self):
        self.customer_check_in_map = defaultdict(CustomerCheckInData)
        self.station_map = defaultdict(StationData)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customer_check_in_map:
            self.customer_check_in_map[id] = CustomerCheckInData(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.customer_check_in_map:
            customer_data = self.customer_check_in_map[id]
            start_station, end_station = customer_data.start_station, stationName
            total_time_taken_to_travel = t - customer_data.start_time
            station_data = self.station_map[(start_station, end_station)]
            station_data.total_travel_time += total_time_taken_to_travel
            station_data.count += 1
            del self.customer_check_in_map[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        station_data = self.station_map[(startStation, endStation)]
        return station_data.total_travel_time / station_data.count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end
