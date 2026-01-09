from functools import reduce

def part1(f):

    file = [line.strip().split() for line in f]
    answer = 0
    for i in range(len(file[0])):
        if file[-1][i] == '+':
            seq_value = 0
            for j in range(len(file)-1):
                seq_value += int(file[j][i])

        elif file[-1][i] == '*':
            seq_value = 1
            for j in range(len(file)-1):
                seq_value *= int(file[j][i])
        
        answer += seq_value
    return answer


def part2(file):
    file = [line.strip('\n') for line in file]
    cols = list(zip(*file))
    cols.insert(0, tuple(' '))
    cols.append(tuple(' '))

    answer = seq_value = 0

    for i, col in enumerate(cols):
        if set(col) == {" "}:
            answer += seq_value
            
            if i < len(cols)-1:
                op = cols[i+1][-1]
            
            seq_value = 0 if op == '+' else 1
        else:
            val = int(''.join(col[:-1]))

            if op == '+':
                seq_value += val
            else:
                seq_value *= val
            
    
    return answer


with open("day6_input") as f:
    file = [line for line in f]        
    print(part1(file))

