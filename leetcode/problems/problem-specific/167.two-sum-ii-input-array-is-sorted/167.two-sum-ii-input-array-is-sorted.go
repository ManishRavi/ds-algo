package main

// * Two Pointer Solution | O(n) Time | O(1) Space

func twoSum(numbers []int, target int) []int {
	numbersSize := len(numbers)
	res := []int{0, 0}
	if numbersSize <= 1 {
		return res
	}

	left, right := 0, numbersSize-1
	for left < right {
		totalSum := numbers[left] + numbers[right]
		if totalSum == target {
			res[0] = left + 1
			res[1] = right + 1
			return res
		} else if totalSum < target {
			left++
		} else {
			right--
		}
	}

	return res
}
