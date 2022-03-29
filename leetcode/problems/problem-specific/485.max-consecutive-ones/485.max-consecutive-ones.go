package main

func findMaxConsecutiveOnes(nums []int) int {
	maxCount, curCount := 0, 0
	for _, v := range nums {
		if v == 1 {
			curCount++
		} else {
			curCount = 0
		}

		if curCount > maxCount {
			maxCount = curCount
		}
	}

	return maxCount
}
