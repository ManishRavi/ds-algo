/*
 * @lc app=leetcode id=501 lang=golang
 *
 * [501] Find Mode in Binary Search Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findMode(root *TreeNode) []int {
	res, sortedSlice := []int{}, []int{}
	inOrder(root, &sortedSlice)
	maxCount, i := 0, 0
	for i < len(sortedSlice) {
		curCount, prevIndex := 1, i
		for i < len(sortedSlice)-1 && sortedSlice[i] == sortedSlice[i+1] {
			i++
		}

		curCount += i - prevIndex
		if curCount > maxCount {
			maxCount = curCount
			res = []int{sortedSlice[i]}
		} else if curCount == maxCount {
			res = append(res, sortedSlice[i])
		}

		i++
	}

	return res
}

func inOrder(root *TreeNode, slice *[]int) {
	if root == nil {
		return
	}

	inOrder(root.Left, slice)
	*slice = append(*slice, root.Val)
	inOrder(root.Right, slice)
}

// @lc code=end

