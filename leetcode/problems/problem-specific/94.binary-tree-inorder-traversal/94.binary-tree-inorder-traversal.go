package main

//  Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	cur, res, stack := root, []int{}, []*TreeNode{}
	for cur != nil || len(stack) > 0 {
		if cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		} else {
			cur = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res = append(res, cur.Val)
			cur = cur.Right
		}
	}

	return res
}

func inorderTraversalRecursive(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	res := []int{}
	inorderTraversalHelper(root, &res)
	return res
}

func inorderTraversalHelper(root *TreeNode, res *[]int) {
	if root == nil {
		return
	}

	inorderTraversalHelper(root.Left, res)
	*res = append(*res, root.Val)
	inorderTraversalHelper(root.Right, res)
}
