searchfile = open("system.log", "r")
for line in searchfile:
    if "BEAR" in line:
        print(line)
    if "X-RAY" in line:
        print(line)
searchfile.close()
