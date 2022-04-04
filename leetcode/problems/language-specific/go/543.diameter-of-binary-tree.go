/*
 * @lc app=leetcode id=543 lang=golang
 *
 * [543] Diameter of Binary Tree
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
func diameterOfBinaryTree(root *TreeNode) int {
	diameter := 0
	diameterOfBinaryTreeHelper(root, &diameter)
	return diameter
}

func diameterOfBinaryTreeHelper(root *TreeNode, diameter *int) int {
	if root == nil {
		return 0
	}

	left := diameterOfBinaryTreeHelper(root.Left, diameter)
	right := diameterOfBinaryTreeHelper(root.Right, diameter)
	*diameter = findMax(*diameter, left+right)
	return 1 + findMax(left, right)
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

