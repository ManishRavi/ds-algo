/*
 * @lc app=leetcode id=203 lang=golang
 *
 * [203] Remove Linked List Elements
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
	if head == nil {
		return head
	}

	prev, cur := head, head
	for cur != nil {
		if cur.Val == val {
			prev.Next = cur.Next
		} else {
			prev = cur
		}

		cur = cur.Next
	}

	if head.Val == val {
		return head.Next
	}

	return head
}

// @lc code=end

