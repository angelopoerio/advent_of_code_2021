package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func IsLowerCase(s string) bool {
	return s == string(strings.ToLower(string(s)))
}

func solve(startNode string, cavesMap map[string][]string, alreadyVisited map[string]bool) int {
	paths := 0

	if startNode == "end" {
		return 1
	}

	for _, cave := range cavesMap[startNode] {
		_, exists := alreadyVisited[cave]
		if !IsLowerCase(cave) || !exists {
			alreadyVisited[cave] = true
			paths += solve(cave, cavesMap, alreadyVisited)
		}
	}

	return paths
}

func main() {
	readFile, err := os.Open("input.txt")

	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	cavesMap := make(map[string][]string)
	memory := make(map[string]bool)

	for fileScanner.Scan() {
		caves := strings.Split(fileScanner.Text(), "-")
		cavesMap[caves[0]] = append(cavesMap[caves[0]], caves[1])
		cavesMap[caves[1]] = append(cavesMap[caves[1]], caves[0])
	}

	defer readFile.Close()

	solution := solve("start", cavesMap, memory)
	fmt.Printf("Solution is %d\n", solution)
}
