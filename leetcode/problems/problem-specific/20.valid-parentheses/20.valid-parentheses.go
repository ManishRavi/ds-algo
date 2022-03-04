package main

func isValid(s string) bool {
	if len(s) <= 1 {
		return false
	}

	stack := []byte{}
	for i := range s {
		if s[i] == '(' || s[i] == '{' || s[i] == '[' {
			stack = append(stack, s[i])
		} else {
			if len(stack) <= 0 ||
				(s[i] == ')' && stack[len(stack)-1] != '(') ||
				(s[i] == '}' && stack[len(stack)-1] != '{') ||
				(s[i] == ']' && stack[len(stack)-1] != '[') {
				return false
			}

			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}
