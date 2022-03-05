package main

func climbStairs(n int) int {
	return stairCase(0, n, make([]int, n+1))
}

func stairCase(start, n int, memcache []int) int {
	if start > n {
		return 0
	}
	if start == n {
		return 1
	}
	if memcache[start] > 0 {
		return memcache[start]
	}

	memcache[start] = stairCase(start+1, n, memcache) + stairCase(start+2, n, memcache)
	return memcache[start]
}

// @lc code=end

func climbStairsIterative(n int) int {
	if n <= 0 {
		return 1
	}

	step1, step2 := 1, 1
	for i := 2; i <= n; i++ {
		sum := step1 + step2
		step1 = step2
		step2 = sum
	}

	return step2
}
