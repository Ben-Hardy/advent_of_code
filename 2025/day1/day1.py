with open('input/input.txt') as f:
    lines = f.read().split("\n")
    dial = 50
    zeroes = 0

    inter_vals = []
    for line in lines:
        direction = line[0]
        value = int(line[1:])
        print(value)

        if direction == "R":
            dial = (dial + value) % 100
        else:
            dial = (dial - value) % 100
        
        if dial == 0:
            zeroes += 1
    print(f"Number of zeroes: {zeroes}")
    