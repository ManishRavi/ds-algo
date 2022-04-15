package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	cur := head.Next
	head.Next = swapPairs(head.Next.Next)
	cur.Next = head
	return cur
}

func swapPairsIterative(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	dummyHead := &ListNode{-1, nil}
	prev, cur := dummyHead, head
	for cur != nil && cur.Next != nil {
		prev.Next = cur.Next
		cur.Next = cur.Next.Next
		prev.Next.Next = cur
		cur = cur.Next
		prev = prev.Next.Next
	}

	return dummyHead.Next
}
