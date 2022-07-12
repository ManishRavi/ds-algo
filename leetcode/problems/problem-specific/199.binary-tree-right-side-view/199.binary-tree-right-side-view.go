package main

/*
 * @lc app=leetcode id=199 lang=golang
 *
 * [199] Binary Tree Right Side View
 */

// @lc code=start

// * Level Order Traversal Solution | O(n) Time | O(n) Space
// * n -> Number of nodes in a tree

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	res, queue := []int{}, []*TreeNode{root}
	for len(queue) > 0 {
		var rightSideNode *TreeNode
		curQueueSize := len(queue)
		for i := 0; i < curQueueSize; i++ {
			curNode := queue[0]
			queue = queue[1:]
			rightSideNode = curNode
			if curNode.Left != nil {
				queue = append(queue, curNode.Left)
			}
			if curNode.Right != nil {
				queue = append(queue, curNode.Right)
			}
		}

		if rightSideNode != nil {
			res = append(res, rightSideNode.Val)
		}
	}

	return res
}

// @lc code=end
