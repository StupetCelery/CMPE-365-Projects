import random
points = int(input("Points Desired: "))
rnge = int(input("Input Highest Desired Point Coordinate: "))
with open("newfile.txt", "w") as f:
	arr = []
	for i in range(points):
		new = (random.randint(0, rnge), random.randint(0, rnge))
		if new not in arr:
			arr.append(new)
		else:
			continue
	
	for i in arr:
		f.write(str(i[0]) + " " + str(i[1]) + "\n")
		
	f.close()
