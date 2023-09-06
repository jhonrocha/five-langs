import os


def parse_elves(filename):
    with open(filename, "r") as f:
        scores = []
        current = 0
        for line in f:
            if line != '\n':
                current += int(line.strip())
            else:
                scores.append(current)
                current = 0
        if current:
            scores.append(current)
    return scores


def challenge1(filename):
    scores = parse_elves(filename)
    return max(scores)


def challenge2(filename):
    scores = parse_elves(filename)
    return sum(sorted(scores)[-3:])


if __name__ == "__main__":
    print("Challenge 1:", challenge1(os.path.join(
        os.path.dirname(__file__), "input.txt")))
    print("Challenge 2:", challenge2(os.path.join(
        os.path.dirname(__file__), "input.txt")))
