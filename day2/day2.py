def part1(ids:[[str]]) -> int:
    answer = 0

    for ranges in ids:
        for i in range(int(ranges[0]), int(ranges[1])+1):
            number = str(i)
            length = len(number)

            for size_sub in range(length//2):
                size_sub += 1

                if length % size_sub > 0:
                    continue

                curr = number[:size_sub]

                if curr == number[size_sub:size_sub*2]:
                    is_id = False
                    for j in range(length // size_sub):
                        next = number[(j)*size_sub:(j+1)*size_sub]

                        if curr != next:
                            is_id = True
                            break

                    if not is_id:
                        answer += i
                        break
                
    return answer

with open("day2_input") as file:
    ids = file.read()
    ids = ids.split(",")

    ids = [id.split("-") for id in ids]

    print(part1(ids))
