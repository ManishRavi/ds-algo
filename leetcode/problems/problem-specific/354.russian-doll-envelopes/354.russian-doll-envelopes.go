package main

import "sort"

// * Binary Search DP Solution | O(nlogn) Time | O(n) Space

func maxEnvelopes(envelopes [][]int) int {
	envelopesSize := len(envelopes)
	// * Sort the envelopes in ascending order based on the width
	sort.Slice(envelopes, func(i, j int) bool {
		// * If both the widths are equal then sort in descending order based on the height
		if envelopes[i][0] == envelopes[j][0] {
			return envelopes[i][1] > envelopes[j][1]
		}

		return envelopes[i][0] < envelopes[j][0]
	})

	maxEnvelopes := 0
	dp := make([]int, envelopesSize)
	for _, v := range envelopes {
		// * Find the index to be inserted based on the height
		index := searchInsert(dp, 0, maxEnvelopes, v[1])
		dp[index] = v[1]
		if index == maxEnvelopes {
			maxEnvelopes++
		}
	}

	return maxEnvelopes
}

func searchInsert(nums []int, left, right, target int) int {
	for left < right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left
}
