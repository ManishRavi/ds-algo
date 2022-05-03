package main

// * O(n) Time | O(1) Space

func sortArrayByParity(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}

	lastEvenDigitIndex := 0
	for i, v := range nums {
		if isEvenDigit(v) {
			nums[lastEvenDigitIndex], nums[i] = nums[i], nums[lastEvenDigitIndex]
			lastEvenDigitIndex++
		}
	}

	return nums
}

func isEvenDigit(n int) bool {
	return n%2 == 0
}
