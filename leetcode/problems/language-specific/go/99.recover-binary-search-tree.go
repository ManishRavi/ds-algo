/*
 * @lc app=leetcode id=99 lang=golang
 *
 * [99] Recover Binary Search Tree
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

var first, second, prev *TreeNode

func recoverTree(root *TreeNode) {
	if root == nil {
		return
	}

	first, second, prev = nil, nil, nil
	inOrder(root)
	first.Val, second.Val = second.Val, first.Val
}

func inOrder(root *TreeNode) {
	if root == nil {
		return
	}

	inOrder(root.Left)
	if first == nil && (prev == nil || prev.Val >= root.Val) {
		first = prev
	}
	if first != nil && prev.Val >= root.Val {
		second = root
	}

	prev = root
	inOrder(root.Right)
}

// @lc code=end

