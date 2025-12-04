with open("input/input.txt") as f:
    lines = f.read().split("\n")
    best = 0
    total = 0
    for line in lines:
        best = 0
        for i in range(len(line) - 2, -1, -1):
            best = max(int(line[i] + str(max([int(j) for j in line[i + 1:]]))), best)
            #print("best: " + str(best) + " cur: " + line[i] + str(max([int(j) for j in line[i + 1:]])))
        total += best
    print(total)