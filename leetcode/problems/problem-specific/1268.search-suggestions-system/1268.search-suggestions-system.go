package main

import (
	"sort"
	"strings"
)

// * Binary Search Solution | O(nlogn) + O(mlogn) Time | O(1) Space

func suggestedProducts(products []string, searchWord string) [][]string {
	productsSize := len(products)
	res, j := make([][]string, len(searchWord)), 0
	sort.Strings(products)
	for i := range searchWord {
		prefix := searchWord[:i+1]
		j = j + sort.SearchStrings(products[j:], prefix)
		cur := []string{}
		for k := 0; k < 3 && j+k < productsSize; k++ {
			if strings.HasPrefix(products[j+k], prefix) {
				cur = append(cur, products[j+k])
			}
		}

		res[i] = cur
	}

	return res
}
