package main

import "math"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	_, isBalanced := isBalancedHelper(root)
	return isBalanced
}

func isBalancedHelper(root *TreeNode) (int, bool) {
	if root == nil {
		return 0, true
	}

	leftSubtreeHeight, isLeftSubtreeBalanced := isBalancedHelper(root.Left)
	rightSubtreeHeight, isRightSubtreeBalanced := isBalancedHelper(root.Right)
	return findMax(leftSubtreeHeight, rightSubtreeHeight) + 1, isLeftSubtreeBalanced && isRightSubtreeBalanced && int(math.Abs(float64(leftSubtreeHeight)-float64(rightSubtreeHeight))) <= 1
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
