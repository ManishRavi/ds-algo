/*
 * @lc app=leetcode id=68 lang=golang
 *
 * [68] Text Justification
 */

// @lc code=start

// * Iterative Solution | O(lines*maxWidth) Time | O(lines*maxWidth) Space

func fullJustify(words []string, maxWidth int) []string {
	res := []string{}
	i, wordsSize := 0, len(words)
	for i < wordsSize {
		j, lineLength := i+1, len(words[i])
		for j < wordsSize && (lineLength+len(words[j])+(j-i-1)) < maxWidth {
			lineLength += len(words[j])
			j++
		}

		diff, numberOfWords := maxWidth-lineLength, j-i
		if numberOfWords == 1 || j >= wordsSize {
			res = append(res, leftJustify(words, diff, i, j))
		} else {
			res = append(res, middleJustify(words, diff, i, j))
		}

		i = j
	}

	return res
}

func middleJustify(words []string, diff, i, j int) string {
	spacesNeeded := j - i - 1
	spaces, extraSpaces := diff/spacesNeeded, diff%spacesNeeded
	var sb strings.Builder
	sb.WriteString(words[i])
	for k := i + 1; k < j; k++ {
		spacesToApply := spaces
		if extraSpaces > 0 {
			spacesToApply += 1
		}

		extraSpaces--
		sb.WriteString(strings.Repeat(" ", spacesToApply) + words[k])
	}

	return sb.String()
}

func leftJustify(words []string, diff, i, j int) string {
	spacesOnRight := diff - (j - i - 1)
	var sb strings.Builder
	sb.WriteString(words[i])
	for k := i + 1; k < j; k++ {
		sb.WriteString(" " + words[k])
	}

	sb.WriteString(strings.Repeat(" ", spacesOnRight))
	return sb.String()
}

// @lc code=end

