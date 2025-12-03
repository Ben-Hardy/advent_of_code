with open('input/input.txt') as f:
    lines = f.read().split("\n")
    dial = 50
    zeroes = 0
    for line in lines:
        direction = line[0]
        value = int(line[1:])

        if value > 100:
            small_chunk = value % 100
            big_chunk = int(value/100)
            zeroes += big_chunk
        else:
            small_chunk = value


        if direction == "R":
            if dial != 0 and dial + small_chunk > 100:
                zeroes += 1
            dial = (dial + small_chunk) % 100
        else:
            if dial != 0 and dial - small_chunk < 0:
                zeroes += 1
            dial = (dial - small_chunk) % 100

        
        if dial == 0:
            zeroes += 1
    print(f"Number of zeroes: {zeroes}")
    