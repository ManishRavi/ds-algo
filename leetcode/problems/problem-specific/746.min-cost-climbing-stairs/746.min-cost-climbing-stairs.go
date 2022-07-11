package main

/*
 * @lc app=leetcode id=746 lang=golang
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start

// * Recursive Memoization Solution | O(n) Time | O(n) Space
// * n -> Length of the cost array

func minCostClimbingStairs(cost []int) int {
	return findMin(minCostClimbingStairsHelper(cost, make([]int, len(cost)+1), 0),
		minCostClimbingStairsHelper(cost, make([]int, len(cost)+1), 1))
}

func minCostClimbingStairsHelper(cost, memcache []int, curStep int) int {
	if curStep >= len(cost) {
		return 0
	}
	if memcache[curStep] > 0 {
		return memcache[curStep]
	}

	memcache[curStep] = cost[curStep] + findMin(minCostClimbingStairsHelper(cost, memcache, curStep+1),
		minCostClimbingStairsHelper(cost, memcache, curStep+2))
	return memcache[curStep]
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

// @lc code=end
