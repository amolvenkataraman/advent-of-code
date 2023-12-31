# Maximum available cubes
MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

ans = 0 # Answer

# Open file and iterate through the lines
with open("input2.txt", "r") as f:
    for line in f.readlines():
        valid = True # Assume game is valid at first
        for draw in line.rstrip().split(": ")[1].split("; "): # Iterate through each individual set of draws
            # Get the number of cubes of each colour and set valid to false if it exceeds the maximum
            for c in [i.split(" ") for i in draw.split(", ")]:
                if int(c[0]) > MAX_CUBES[c[1]]: valid = False
        
        if valid: ans += int(line.split(": ")[0].split(" ")[1]) # Update the final answer if the game is valid

print(ans)
