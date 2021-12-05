package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func solve(lines []string) int {
	depth := 0
	horizontalPosition := 0

	for _, line := range lines {
		var offset int
		var command string
		_, err := fmt.Sscanf(line, "%s %d", &command, &offset)

		if err != nil {
			panic(fmt.Sprintf("Invalid line: %s. Error: %v", line, err))
		}

		switch command {
		case "forward":
			horizontalPosition += offset
		case "up":
			depth -= offset
		case "down":
			depth += offset
		}
	}

	return depth * horizontalPosition

}

func main() {
	readFile, err := os.Open("input")

	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	var Lines []string

	for fileScanner.Scan() {
		Lines = append(Lines, fileScanner.Text())
	}

	defer readFile.Close()

	solution := solve(Lines)
	fmt.Printf("Solution is %d\n", solution)
}
