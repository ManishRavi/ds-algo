package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	res := 0
	sumOfLeftLeavesHelper(root, false, &res)
	return res
}

func sumOfLeftLeavesHelper(root *TreeNode, isLeftNode bool, res *int) {
	if root.Left == nil && root.Right == nil && isLeftNode {
		*res += root.Val
		return
	}

	if root.Left != nil {
		sumOfLeftLeavesHelper(root.Left, true, res)
	}
	if root.Right != nil {
		sumOfLeftLeavesHelper(root.Right, false, res)
	}
}
