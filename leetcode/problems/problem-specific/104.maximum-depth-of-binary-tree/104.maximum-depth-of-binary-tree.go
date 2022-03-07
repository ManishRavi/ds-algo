package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return findMax(maxDepth(root.Left), maxDepth(root.Right)) + 1
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
