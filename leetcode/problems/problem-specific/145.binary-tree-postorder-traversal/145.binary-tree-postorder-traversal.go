package main

//  Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func postorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	res := []int{}
	postorderTraversalHelper(root, &res)
	return res
}

func postorderTraversalHelper(root *TreeNode, res *[]int) {
	if root == nil {
		return
	}

	postorderTraversalHelper(root.Left, res)
	postorderTraversalHelper(root.Right, res)
	*res = append(*res, root.Val)
}
