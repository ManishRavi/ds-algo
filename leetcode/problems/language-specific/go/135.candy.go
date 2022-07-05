/*
 * @lc app=leetcode id=135 lang=golang
 *
 * [135] Candy
 */

// @lc code=start

// * Two Pass Solution | O(n) Time | O(n) Space
// * n -> Length of the ratings array

func candy(ratings []int) int {
	ratingsSize := len(ratings)
	candies := make([]int, ratingsSize)
	for i := range candies {
		candies[i] = 1
	}

	// * Forward Pass
	for i := 1; i < ratingsSize; i++ {
		if ratings[i] > ratings[i-1] {
			candies[i] = candies[i-1] + 1
		}
	}

	minCandies := candies[ratingsSize-1]
	// * Backward Pass
	for i := ratingsSize - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] {
			candies[i] = findMax(candies[i], candies[i+1]+1)
		}

		minCandies += candies[i]
	}

	return minCandies
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

