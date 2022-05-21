package main

import "regexp"

// * Regex Solution

func isNumber(s string) bool {
	reg, _ := regexp.Compile("^[+-]?(\\d+(\\.\\d*)?|\\.\\d+)([eE][+-]?\\d+)?$")
	return reg.MatchString(s)
}
