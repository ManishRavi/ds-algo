package main

type MyHashSet struct {
	slice []bool
}

func Constructor() MyHashSet {
	return MyHashSet{make([]bool, 1000001)}
}

func (this *MyHashSet) Add(key int) {
	this.slice[key] = true
}

func (this *MyHashSet) Remove(key int) {
	this.slice[key] = false
}

func (this *MyHashSet) Contains(key int) bool {
	return this.slice[key]
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
