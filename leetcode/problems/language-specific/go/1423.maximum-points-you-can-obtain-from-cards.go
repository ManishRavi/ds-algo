/*
 * @lc app=leetcode id=1423 lang=golang
 *
 * [1423] Maximum Points You Can Obtain from Cards
 */

// @lc code=start

// * Sliding Window Solution | O(k) Time | O(1) Space

func maxScore(cardPoints []int, k int) int {
	cardPointsSize := len(cardPoints)
	left, right := 0, cardPointsSize-k
	nonWindowSum := 0
	for i := right; i < cardPointsSize; i++ {
		nonWindowSum += cardPoints[i]
	}

	maxScore := nonWindowSum
	for right < cardPointsSize {
		nonWindowSum += cardPoints[left] - cardPoints[right]
		maxScore = findMax(maxScore, nonWindowSum)
		left++
		right++
	}

	return maxScore
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

