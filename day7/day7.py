
def get_splits(file):
    beams_location = set()
    splits = 0

    for line in file:
        beams_location.add(line.index("S"))
        break

    for line in file:
        line = line.strip()

        new_beams = beams_location.copy()

        for pos in beams_location:
            if line[pos] == "^":
                new_beams.add(pos-1)
                new_beams.add(pos+1)

                new_beams.remove(pos)

                splits += 1

        beams_location = new_beams

        for l in beams_location:
            line = line[:l] + "|" + line[l+1:]
            
        print(line)
        
    return splits

def get_timelines(file):
    beams_location = {}

    for line in file:
        beams_location[line.index("S")] = 1
        break

    for line in file:
        new_beams = {}

        for pos, count in beams_location.items():
            if line[pos] == "^":
                new_beams[pos+1] = count + new_beams.get(pos+1, 0)
                new_beams[pos-1] = count + new_beams.get(pos-1, 0)
            else:
                new_beams[pos] = count + new_beams.get(pos, 0)
        
        beams_location = new_beams

    return sum(beams_location.values())

if __name__ == '__main__':
    with open("day7_input") as file:
        print("splits: ", get_splits(file))

    with open("day7_input") as file:
        print("timelines: ", get_timelines(file))
