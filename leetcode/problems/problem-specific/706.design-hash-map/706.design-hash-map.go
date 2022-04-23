package main

type MyHashMap struct {
	slice []int
}

func Constructor() MyHashMap {
	return MyHashMap{make([]int, 1000001)}
}

func (this *MyHashMap) Put(key int, value int) {
	this.slice[key] = value + 1
}

func (this *MyHashMap) Get(key int) int {
	return this.slice[key] - 1
}

func (this *MyHashMap) Remove(key int) {
	this.slice[key] = 0
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
