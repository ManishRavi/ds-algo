package main

func maxArea(height []int) int {
	res, left, right := 0, 0, len(height)-1
	for left < right {
		// * Area of rectangle = length * width
		area := findMin(height[left], height[right]) * (right - left)
		res = findMax(res, area)
		// * Move the shorter height pointer
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return res
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}
