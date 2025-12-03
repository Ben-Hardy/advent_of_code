with open("input/input.txt") as f:
    data = f.read().split(",")
    total = 0
    for val in data:
        lo, hi = val.split("-")
        print(f"{lo}, {hi}")
        nums = range(int(lo), int(hi) + 1)
        for num in nums:
            num = str(num)
            if num[:len(num)//2] == num[len(num)//2:]:
                total += int(num)

    print(total)