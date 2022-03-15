/*
 * @lc app=leetcode id=206 lang=golang
 *
 * [206] Reverse Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	cur, dummyHead := head, &ListNode{
		Val:  -1,
		Next: nil,
	}

	for cur != nil {
		next := cur.Next
		cur.Next = dummyHead.Next
		dummyHead.Next = cur
		cur = next
	}

	return dummyHead.Next
}

// @lc code=end

func reverseListRecursive(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	prev := head
	head = reverseListRecursive(head.Next)
	prev.Next.Next = prev
	prev.Next = nil
	return head
}
