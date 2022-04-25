/*
 * @lc app=leetcode id=1396 lang=golang
 *
 * [1396] Design Underground System
 */

// @lc code=start
type UndergroundSystem struct {
	customerCheckInMappings map[int]CheckInData
	stationMappings         map[string]StationData
}

type CheckInData struct {
	startStation string
	startTime    int
}

type StationData struct {
	totalTime int
	count     int
}

func Constructor() UndergroundSystem {
	return UndergroundSystem{map[int]CheckInData{}, map[string]StationData{}}
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	if _, ok := this.customerCheckInMappings[id]; !ok {
		this.customerCheckInMappings[id] = CheckInData{stationName, t}
	}
}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	if customerCheckInData, ok := this.customerCheckInMappings[id]; ok {
		startEndStation := fmt.Sprintf("%v_%v", customerCheckInData.startStation, stationName)
		totalTimeTakenToTravel := t - customerCheckInData.startTime
		stationData := this.stationMappings[startEndStation]
		this.stationMappings[startEndStation] = StationData{stationData.totalTime + totalTimeTakenToTravel, stationData.count + 1}
		delete(this.customerCheckInMappings, id)
	}
}

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	startEndStation := fmt.Sprintf("%v_%v", startStation, endStation)
	if stationData, ok := this.stationMappings[startEndStation]; ok {
		return float64(stationData.totalTime) / float64(stationData.count)
	}

	return 0.00
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */
// @lc code=end

