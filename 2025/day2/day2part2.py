with open("input/smallinput.txt") as f:
    data = f.read().split(",")
    total = 0
    counted = []
    for val in data:
        lo, hi = val.split("-")
        nums = range(int(lo), int(hi) + 1)
        for num in nums:
            num = str(num)
            for i in range(1,len(num)):
                chunk = num[0:i]
                if "".join(num.split(chunk)) == '': # fun trick. It creates a list with empty strings.
                    total += int(num)               # any non-matches add a number to the list so they can be ignored
                    counted.append(num)             # eg. 824824824 split with 824 creates ['','','']
                    break                           # while 824824825 split with 824 creates ['','','825'], which can be
    print(counted)                                  # safely ignored
    print(total)