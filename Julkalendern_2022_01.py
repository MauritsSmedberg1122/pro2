calorielist = []
with open("input.txt", "rt") as f:
    lines = [i for i in f.read().strip().split("\n")]
max = 0
count = 0
for line in lines:
    if line == "":
        
        calorielist.append(count)
        count = 0
    else:
        calorienum = int(line)
        count += calorienum

        if count > max:
            print(f"Highest calories is: {count}")
            max = count
            
