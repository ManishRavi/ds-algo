package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// * Iterative Solution | O(n) Time | O(1) Space

func reverseKGroup(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	dummyHead := &ListNode{0, head}
	prevGroup := dummyHead
	for {
		kthNode := getKthNode(prevGroup, k)
		if kthNode == nil {
			break
		}

		// * Reverse the nodes in the current group
		nextGroup := kthNode.Next
		prev, cur := kthNode.Next, prevGroup.Next
		for cur != nextGroup {
			next := cur.Next
			cur.Next = prev
			prev = cur
			cur = next
		}

		// * Modify the prevGroup link
		next := prevGroup.Next
		prevGroup.Next = kthNode
		prevGroup = next
	}

	return dummyHead.Next
}

func getKthNode(head *ListNode, k int) *ListNode {
	for head != nil && k > 0 {
		head = head.Next
		k -= 1
	}

	return head
}
