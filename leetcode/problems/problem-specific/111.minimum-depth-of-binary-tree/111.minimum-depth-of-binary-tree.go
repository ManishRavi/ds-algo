package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	left, right := minDepth(root.Left), minDepth(root.Right)
	if left == 0 || right == 0 {
		return left + right + 1
	}

	return findMin(left, right) + 1
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}
