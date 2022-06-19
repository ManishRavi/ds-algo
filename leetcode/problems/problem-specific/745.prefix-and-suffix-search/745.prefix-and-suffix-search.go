package main

import "fmt"

type WordFilter struct {
	WordMappings map[string]int
}

func Constructor(words []string) WordFilter {
	wordMappings := make(map[string]int, len(words)*100)
	for i, v := range words {
		for left := 1; left <= 10 && left <= len(v); left++ {
			for right := 1; right <= 10 && right <= len(v); right++ {
				wordMappings[fmt.Sprintf("%v-%v", v[:left], v[len(v)-right:])] = i
			}
		}
	}

	return WordFilter{wordMappings}
}

func (this *WordFilter) F(prefix string, suffix string) int {
	if v, ok := this.WordMappings[fmt.Sprintf("%v-%v", prefix, suffix)]; ok {
		return v
	}

	return -1
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.F(prefix,suffix);
 */
