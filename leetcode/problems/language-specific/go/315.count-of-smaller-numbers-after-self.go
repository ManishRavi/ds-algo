/*
 * @lc app=leetcode id=315 lang=golang
 *
 * [315] Count of Smaller Numbers After Self
 */

// @lc code=start

// * Merge Sort Solution | O(nlogn) Time | O(n) Space
// * n -> Length of nums array

type Pair struct {
	Val   int
	Index int
}

func countSmaller(nums []int) []int {
	numsSize := len(nums)
	counts := make([]int, numsSize)
	numsIndex := make([]Pair, numsSize)
	for i, v := range nums {
		numsIndex[i] = Pair{v, i}
	}

	mergeSort(counts, numsIndex, 0, numsSize-1)
	return counts
}

func mergeSort(counts []int, numsIndex []Pair, left, right int) {
	if left < right {
		mid := left + (right-left)/2
		mergeSort(counts, numsIndex, left, mid)
		mergeSort(counts, numsIndex, mid+1, right)
		merge(counts, numsIndex, left, mid, right)
	}
}

func merge(counts []int, numsIndex []Pair, left, mid, right int) {
	temp := make([]Pair, right-left+1)
	i, j, k := left, mid+1, 0
	for i <= mid && j <= right {
		if numsIndex[i].Val <= numsIndex[j].Val {
			temp[k] = numsIndex[j]
			j++
		} else {
			counts[numsIndex[i].Index] += right - j + 1
			temp[k] = numsIndex[i]
			i++
		}

		k++
	}

	for i <= mid {
		temp[k] = numsIndex[i]
		i++
		k++
	}
	for j <= right {
		temp[k] = numsIndex[j]
		j++
		k++
	}

	for i := left; i <= right; i++ {
		numsIndex[i] = temp[i-left]
	}
}

// @lc code=end

