with open("aoc3.txt", "r") as f:
    lines = f.readlines()

lines = [line.replace(";", ",").replace(" ", "").replace("reen", "").replace("ed", "").replace("lue", "").strip().split(":")[1] for line in lines]

summ = 0
for idx, val in enumerate(lines):
    blimit = 0
    glimit = 0
    rlimit = 0
    vals = val.split(",")
    print(vals)
    flag = 1
    for i in vals:
        if ( i[-1] == "g" and int(i[0:-1]) > glimit ):
            glimit = int(i[0:-1])
        if ( i[-1] == "b" and int(i[0:-1]) > blimit ):
            blimit = int(i[0:-1])
        if ( i[-1] == "r" and int(i[0:-1]) > rlimit ):
            rlimit = int(i[0:-1])
    
    summ += (blimit * rlimit * glimit)

print(summ)