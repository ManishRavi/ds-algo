package main

// * Two Pointer Solution | O(n) Time | O(1) Space

func trap(height []int) int {
	heightSize := len(height)
	if heightSize <= 2 {
		return 0
	}

	res := 0
	left, right := 0, heightSize-1
	leftMax, rightMax := 0, 0
	for left < right {
		// * Left Half
		if height[left] <= height[right] {
			if height[left] >= leftMax {
				leftMax = height[left]
			} else {
				res += leftMax - height[left]
			}

			left++
		} else {
			// * Rigth Half
			if height[right] >= rightMax {
				rightMax = height[right]
			} else {
				res += rightMax - height[right]
			}

			right--
		}
	}

	return res
}
