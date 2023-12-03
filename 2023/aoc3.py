with open("aoc3.txt", "r") as f:
    lines = f.readlines()

lines = [line.replace(";", ",").replace(" ", "").replace("reen", "").replace("ed", "").replace("lue", "").strip().split(":")[1] for line in lines]

blimit = 14
glimit = 13
rlimit = 12

sum = 0
for idx, val in enumerate(lines):
    vals = val.split(",")
    print(vals)
    flag = 1
    for i in vals:
        if ( i[-1] == "g" and int(i[0:-1]) > glimit ) or \
            ( i[-1] == "b" and int(i[0:-1]) > blimit ) or \
            ( i[-1] == "r" and int(i[0:-1]) > rlimit ):
                 flag = 0
    
    if flag == 1:
         sum += idx+1

print(sum)