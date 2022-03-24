package main

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
	if n == 1 {
		return n
	}

	left, right := 1, n
	for left <= right {
		mid := left + (right-left)/2
		guessVal := guess(mid)
		if guessVal == 0 {
			return mid
		} else if guessVal == 1 {
			left = mid + 1
		} else if guessVal == -1 {
			right = mid - 1
		}
	}

	return -1
}

func guess(num int) int {
	return 1
}
