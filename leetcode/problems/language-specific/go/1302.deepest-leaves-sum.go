/*
 * @lc app=leetcode id=1302 lang=golang
 *
 * [1302] Deepest Leaves Sum
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

// * Recursive Solution | O(n) Time | O(h) Space

func deepestLeavesSum(root *TreeNode) int {
	if root == nil {
		return 0
	}

	// * Find max-depth of a tree
	maxDepth := findMaxDepth(root)
	return deepestLeavesSumHelper(root, maxDepth, 1)
}

func findMaxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return 1 + findMax(findMaxDepth(root.Left), findMaxDepth(root.Right))
}

func deepestLeavesSumHelper(root *TreeNode, maxDepth, curDepth int) int {
	if root == nil {
		return 0
	}
	if root.Left == nil && root.Right == nil && curDepth == maxDepth {
		return root.Val
	}

	return deepestLeavesSumHelper(root.Left, maxDepth, curDepth+1) +
		deepestLeavesSumHelper(root.Right, maxDepth, curDepth+1)
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

