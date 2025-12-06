pos = 50
password = 0

with open("day1_input") as file:
    for cmd in file:
        steps = int(cmd[1:])

        x = 1 if cmd[0] == "R" else -1
        
        for _ in range(steps):
            pos = (pos + x) % 100
            if pos == 0:
                password += 1

print(password)