/*
 * @lc app=leetcode id=101 lang=golang
 *
 * [101] Symmetric Tree
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
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	queue := []*TreeNode{root.Left, root.Right}
	for len(queue) > 1 {
		left, right := queue[0], queue[1]
		queue = queue[2:]
		if left == nil && right == nil {
			continue
		}
		if left == nil || right == nil || left.Val != right.Val {
			return false
		}

		queue = append(queue, left.Left, right.Right, left.Right, right.Left)
	}

	return true
}

// @lc code=end

func isSymmetricRecursive(root *TreeNode) bool {
	if root == nil {
		return true
	}

	return isSymmetricHelperRecursive(root.Left, root.Right)
}

func isSymmetricHelperRecursive(left *TreeNode, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	}
	if left == nil || right == nil || left.Val != right.Val {
		return false
	}

	return isSymmetricHelperRecursive(left.Left, right.Right) && isSymmetricHelperRecursive(left.Right, right.Left)
}
