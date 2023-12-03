with open(r"C:\Users\soaib\Documents\Projects\advent-of-code\2023\aoc5.txt", "r") as f:
    lines = f.readlines()
    
lines = [line.strip() for line in lines]

sum = 0
for idx, i in enumerate(lines):
    idy = 0
    while idy < len(i):
        flag = 0
        init = idy

        if lines[idx][idy].isdigit():
            while idy < len(lines[idx]) and lines[idx][idy].isdigit():
                idy+=1

            if (idx-1) >= 0:
                if (init-1) >= 0 and ( lines[idx-1][init-1].isdigit() is False and lines[idx-1][init-1] != '.' ):
                    flag = 1
                    
                if (idy) < len(i) and ( lines[idx-1][idy].isdigit() is False and lines[idx-1][idy] != '.' ):
                    flag = 1

                if flag != 1:
                    for z in lines[idx-1][init:idy]:
                        if z.isdigit() is False and z != '.':
                            flag = 1
                            break

            if (idx+1) < len(lines):
                if (init-1) >= 0 and ( lines[idx+1][init-1].isdigit() is False and lines[idx+1][init-1] != '.' ):
                    flag = 1
                    
                if (idy) < len(i) and ( lines[idx+1][idy].isdigit() is False and lines[idx+1][idy] != '.' ):
                    flag = 1

                if flag != 1:
                    for z in lines[idx+1][init:idy]:
                        if z.isdigit() is False and z != '.':
                            flag = 1
                            break

            if (init-1) >= 0 and ( lines[idx][init-1].isdigit() is False and lines[idx][init-1] != '.' ):
                flag = 1

            if (idy+1) < len(i) and ( lines[idx][idy].isdigit() is False and lines[idx][idy] != '.' ):
                flag = 1

        if flag == 1:
            print(int(lines[idx][init:idy]))
            sum += int(lines[idx][init:idy])
        idy += 1


print(sum)