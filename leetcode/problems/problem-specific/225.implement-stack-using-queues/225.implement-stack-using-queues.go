package main

type MyStack struct {
	Dequeue []int
}

func Constructor() MyStack {
	return MyStack{}
}

func (this *MyStack) Push(x int) {
	this.Dequeue = append(this.Dequeue, x)
}

func (this *MyStack) Pop() int {
	el := this.Dequeue[len(this.Dequeue)-1]
	this.Dequeue = this.Dequeue[:len(this.Dequeue)-1]
	return el
}

func (this *MyStack) Top() int {
	return this.Dequeue[len(this.Dequeue)-1]
}

func (this *MyStack) Empty() bool {
	return len(this.Dequeue) <= 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
