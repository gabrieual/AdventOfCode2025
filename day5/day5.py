def part1(file):
    ranges = []
    answer = 0
    for line in file:
        if "-" in line:
            init, end = line.split("-")            
            ranges.append((int(init), int(end)))

        elif line != '\n':
            num = int(line)
            for init, end in ranges:
                if num >= init and num <= end:
                    answer += 1
                    break
    return answer

def part2(file):
    ranges = []
    answer = 0
    for line in file:
        if "-" in line:
            init, end = line.split("-")
            ranges.append((int(init), int(end)))

    ranges.sort()
    m = 0
    while (m < len(ranges)-1 ):
        init, end = ranges[m]
        i, e = ranges[m+1]
        
        if end >= i:
            end = max(end, e)
            ranges[m+1] = (init, end)
            ranges.pop(m)

        else:
            m += 1        

    for init, end in ranges:
        answer += end - init + 1 

    return answer
        


with open("day5_input") as file:
    print(part1(file))
    print(part2(file))
