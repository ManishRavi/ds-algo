/*
 * @lc app=leetcode id=399 lang=golang
 *
 * [399] Evaluate Division
 */

// @lc code=start
var exists = struct{}{}

type Node struct {
	Key string
	Val float64
}

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	graph := buildGraph(equations, values)
	res := make([]float64, len(queries))
	for i := 0; i < len(queries); i++ {
		src, dest := queries[i][0], queries[i][1]
		res[i] = calcEquationHelperDFS(src, dest, map[string]struct{}{}, graph)
	}

	return res
}

func buildGraph(equations [][]string, values []float64) map[string][]Node {
	graph := map[string][]Node{}
	for i := 0; i < len(equations); i++ {
		src, dest := equations[i][0], equations[i][1]
		graph[src] = append(graph[src], Node{dest, values[i]})
		graph[dest] = append(graph[dest], Node{src, 1 / values[i]})
	}

	return graph
}

func calcEquationHelperDFS(src, dest string, visited map[string]struct{}, graph map[string][]Node) float64 {
	_, srcOk := graph[src]
	_, destOk := graph[dest]
	if !srcOk && !destOk {
		return -1.0
	}
	if src == dest {
		return 1.0
	}

	visited[src] = exists
	for _, v := range graph[src] {
		if _, visitedOk := visited[v.Key]; !visitedOk {
			res := calcEquationHelperDFS(v.Key, dest, visited, graph)
			if res != -1.0 {
				return res * v.Val
			}
		}
	}

	return -1.0
}

// @lc code=end

