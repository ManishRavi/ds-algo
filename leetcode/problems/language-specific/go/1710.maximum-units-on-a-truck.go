/*
 * @lc app=leetcode id=1710 lang=golang
 *
 * [1710] Maximum Units on a Truck
 */

// @lc code=start

// * Sorting Based Solution | O(nlogn) Time | O(1) Space
// * n -> Total number of box types

func maximumUnits(boxTypes [][]int, truckSize int) int {
	sort.Slice(boxTypes, func(i, j int) bool {
		return boxTypes[i][1] > boxTypes[j][1]
	})

	maxTotalUnits := 0
	for _, box := range boxTypes {
		if truckSize > 0 {
			numberOfBoxes, numberOfUnitsPerBox := box[0], box[1]
			numberOfBoxesPicked := findMin(numberOfBoxes, truckSize)
			maxTotalUnits += numberOfBoxesPicked * numberOfUnitsPerBox
			truckSize = int(math.Abs(float64(truckSize - numberOfBoxesPicked)))
		} else {
			break
		}
	}

	return maxTotalUnits
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

// @lc code=end

