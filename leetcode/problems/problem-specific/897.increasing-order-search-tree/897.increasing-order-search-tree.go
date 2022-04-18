package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var prev *TreeNode

func increasingBST(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}

	dummyRoot := &TreeNode{-1, nil, nil}
	prev = dummyRoot
	inOrder(root)
	return dummyRoot.Right
}

func inOrder(root *TreeNode) {
	if root == nil {
		return
	}

	inOrder(root.Left)
	prev.Right = root
	prev = root
	prev.Left = nil
	inOrder(root.Right)
}
