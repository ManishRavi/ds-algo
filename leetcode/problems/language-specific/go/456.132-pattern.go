/*
 * @lc app=leetcode id=456 lang=golang
 *
 * [456] 132 Pattern
 */

// @lc code=start

// * O(n) Time | O(n) Space

type Pair struct {
	Key     int
	PrevMin int
}

func find132pattern(nums []int) bool {
	numsSize := len(nums)
	if numsSize < 3 {
		return false
	}

	stack := []Pair{}
	curMin := nums[0]
	for _, v := range nums[1:] {
		for len(stack) > 0 && v >= stack[len(stack)-1].Key {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 && v > stack[len(stack)-1].PrevMin {
			return true
		}

		stack = append(stack, Pair{v, curMin})
		curMin = findMin(curMin, v)
	}

	return false
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

// @lc code=end

