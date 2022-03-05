/*
 * @lc app=leetcode id=144 lang=golang
 *
 * [144] Binary Tree Preorder Traversal
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
func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	cur, res, stack := root, []int{}, []*TreeNode{}
	for cur != nil || len(stack) > 0 {
		if cur != nil {
			res = append(res, cur.Val)
			stack = append(stack, cur)
			cur = cur.Left
		} else {
			cur = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			cur = cur.Right
		}
	}

	return res
}

// @lc code=end

func preorderTraversalRecursive(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	res := []int{}
	preorderTraversalHelper(root, &res)
	return res
}

func preorderTraversalHelper(root *TreeNode, res *[]int) {
	if root == nil {
		return
	}

	*res = append(*res, root.Val)
	preorderTraversalHelper(root.Left, res)
	preorderTraversalHelper(root.Right, res)
}
