package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

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
