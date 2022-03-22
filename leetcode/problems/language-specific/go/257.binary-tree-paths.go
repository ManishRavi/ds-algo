/*
 * @lc app=leetcode id=257 lang=golang
 *
 * [257] Binary Tree Paths
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
func binaryTreePaths(root *TreeNode) []string {
	if root == nil {
		return []string{}
	}

	res := []string{}
	binaryTreePathsHelper(root, &res, fmt.Sprintf("%v", root.Val))
	return res
}

func binaryTreePathsHelper(root *TreeNode, res *[]string, s string) {
	if root.Left == nil && root.Right == nil {
		*res = append(*res, s)
		return
	}

	if root.Left != nil {
		binaryTreePathsHelper(root.Left, res, fmt.Sprintf("%v->%v", s, root.Left.Val))
	}
	if root.Right != nil {
		binaryTreePathsHelper(root.Right, res, fmt.Sprintf("%v->%v", s, root.Right.Val))
	}
}

// @lc code=end

