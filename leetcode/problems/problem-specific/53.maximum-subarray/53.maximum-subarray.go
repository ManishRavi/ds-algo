package main

func maxSubArray(nums []int) int {
	if len(nums) <= 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}

	largestSum, intermediateSum := nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		intermediateSum = findMax(nums[i], nums[i]+intermediateSum)
		if intermediateSum > largestSum {
			largestSum = intermediateSum
		}
	}

	return largestSum
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
