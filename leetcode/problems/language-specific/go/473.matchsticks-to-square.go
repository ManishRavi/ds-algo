/*
 * @lc app=leetcode id=473 lang=golang
 *
 * [473] Matchsticks to Square
 */

// @lc code=start

// * Backtracking Solution | O(4^n) Time | O(n) Space
// * n -> Total length of the matchsticks array

func makesquare(matchsticks []int) bool {
	matchsticksSize, matchsticksSum := len(matchsticks), findSum(matchsticks)
	if matchsticksSum%4 != 0 {
		return false
	}

	squareSideLength := int(matchsticksSum / 4)
	sides := make([]int, 4)
	sort.Slice(matchsticks, func(i, j int) bool {
		return matchsticks[i] > matchsticks[j]
	})

	var makesquareHelper func(curIndex int) bool
	makesquareHelper = func(curIndex int) bool {
		if curIndex == matchsticksSize {
			return true
		}

		for i := 0; i < 4; i++ {
			if sides[i]+matchsticks[curIndex] <= squareSideLength {
				sides[i] += matchsticks[curIndex]
				if makesquareHelper(curIndex + 1) {
					return true
				}

				sides[i] -= matchsticks[curIndex]
			}
		}

		return false
	}

	return makesquareHelper(0)
}

func findSum(nums []int) int {
	totalSum := 0
	for _, v := range nums {
		totalSum += v
	}

	return totalSum
}

// @lc code=end

