package main

// Below is the interface for Iterator, which is already defined for you by LeetCode.

type Iterator struct {
}

func (this *Iterator) hasNext() bool {
	// Returns true if the iteration has more elements.
	return true
}

func (this *Iterator) next() int {
	// Returns the next element in the iteration.
	return 0
}

type PeekingIterator struct {
	iter    *Iterator
	nextVal int
}

func Constructor(iter *Iterator) *PeekingIterator {
	n := 0
	if iter.hasNext() {
		n = iter.next()
	}

	return &PeekingIterator{iter, n}
}

func (this *PeekingIterator) hasNext() bool {
	return this.nextVal != 0 || this.iter.hasNext()
}

func (this *PeekingIterator) next() int {
	curVal := this.nextVal
	if this.iter.hasNext() {
		this.nextVal = this.iter.next()
	} else {
		this.nextVal = 0
	}

	return curVal
}

func (this *PeekingIterator) peek() int {
	return this.nextVal
}
