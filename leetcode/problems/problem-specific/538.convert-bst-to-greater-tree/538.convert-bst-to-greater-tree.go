package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func convertBST(root *TreeNode) *TreeNode {
	totalSum := 0
	convertBSTHelper(root, &totalSum)
	return root
}

func convertBSTHelper(root *TreeNode, totalSum *int) {
	if root == nil {
		return
	}

	convertBSTHelper(root.Right, totalSum)
	*totalSum += root.Val
	root.Val = *totalSum
	convertBSTHelper(root.Left, totalSum)
}
