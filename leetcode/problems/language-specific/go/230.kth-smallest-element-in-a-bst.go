/*
 * @lc app=leetcode id=230 lang=golang
 *
 * [230] Kth Smallest Element in a BST
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
func kthSmallest(root *TreeNode, k int) int {
	curIndex := 0
	kthNode := inOrder(root, k, &curIndex)
	return kthNode.Val
}

func inOrder(root *TreeNode, k int, curIndex *int) *TreeNode {
	if root == nil {
		return root
	}

	left := inOrder(root.Left, k, curIndex)
	if left != nil {
		return left
	}

	*curIndex++
	if *curIndex == k {
		return root
	}

	return inOrder(root.Right, k, curIndex)
}

// @lc code=end

