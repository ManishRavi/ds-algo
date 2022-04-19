package main

func jump(nums []int) int {
	if len(nums) <= 0 {
		return 0
	}

	minJumps, curEnd, curFarthest := 0, 0, 0
	for i := 0; i < len(nums)-1; i++ {
		curFarthest = findMax(curFarthest, i+nums[i])
		if i == curEnd {
			curEnd = curFarthest
			minJumps++
		}
	}

	return minJumps
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
