package main

/*
 * @lc app=leetcode id=128 lang=golang
 *
 * [128] Longest Consecutive Sequence
 */

// @lc code=start

// * HashSet and Intelligent Sequence Building Solution | O(n) Time | O(n) Space
// * n -> Length of the nums array

func longestConsecutive(nums []int) int {
	numsSize := len(nums)
	if numsSize <= 1 {
		return numsSize
	}

	var exists = struct{}{}
	mappings, longestConsecutiveSequence := make(map[int]struct{}), 0
	for _, num := range nums {
		mappings[num] = exists
	}

	for _, num := range nums {
		// * Check if it's the start of the sequence
		if _, ok := mappings[num-1]; !ok {
			curElement, curSequenceSize := num, 1
			for {
				if _, ok := mappings[curElement+1]; ok {
					curElement += 1
					curSequenceSize += 1
				} else {
					break
				}
			}

			longestConsecutiveSequence = findMax(longestConsecutiveSequence, curSequenceSize)
		}
	}

	return longestConsecutiveSequence
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end
