package main

/*
 * @lc app=leetcode id=509 lang=golang
 *
 * [509] Fibonacci Number
 */

// @lc code=start

// * Recursive Memoization Solution | O(n) Time | O(n) Space
// * n -> n

func fib(n int) int {
	if n <= 1 {
		return n
	}

	memcache := make([]int, n+1)
	memcache[1] = 1
	return fibHelper(n, memcache)
}

func fibHelper(n int, memcache []int) int {
	if n <= 1 {
		return n
	}
	if memcache[n] > 0 {
		return memcache[n]
	}

	memcache[n] = fibHelper(n-1, memcache) + fibHelper(n-2, memcache)
	return memcache[n]
}

// @lc code=end

// * Iterative Solution | O(n) Time | O(1) Space
// * n -> n

func fibIterative(n int) int {
	if n <= 1 {
		return n
	}

	res, a, b := 1, 0, 1
	for i := 2; i <= n; i++ {
		res = a + b
		a, b = b, res
	}

	return res
}
