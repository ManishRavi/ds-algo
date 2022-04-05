/*
 * @lc app=leetcode id=1721 lang=golang
 *
 * [1721] Swapping Nodes in a Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapNodes(head *ListNode, k int) *ListNode {
	// 1. Find the k-th node from the front which is left
	// 2. Make left node as the current node, right node from the front,
	//    when the current node reach end, right node is just the k-th last element
	// 3. Swap their values

	left, right, curCount := head, head, 0
	for left != nil {
		curCount++
		if curCount == k {
			break
		}

		left = left.Next
	}

	cur := left
	for cur.Next != nil {
		cur = cur.Next
		right = right.Next
	}

	left.Val, right.Val = right.Val, left.Val
	return head
}

// @lc code=end

