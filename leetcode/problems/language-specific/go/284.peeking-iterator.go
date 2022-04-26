/*
 * @lc app=leetcode id=284 lang=golang
 *
 * [284] Peeking Iterator
 */

// @lc code=start
/*   Below is the interface for Iterator, which is already defined for you.
 *
 *   type Iterator struct {
 *
 *   }
 *
 *   func (this *Iterator) hasNext() bool {
 *		// Returns true if the iteration has more elements.
 *   }
 *
 *   func (this *Iterator) next() int {
 *		// Returns the next element in the iteration.
 *   }
 */

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

// @lc code=end

