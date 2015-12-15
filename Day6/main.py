inp = open('input', 'r').read().split("\n");

bigLights = [];
for i in range(0,1000):
	tmp = [];
	for i2 in range(0,1000):
		tmp.append(0);
	bigLights.append(tmp);

def parseInstr(instr):
	instr = instr.split(" ");
	if instr[1] == "on":
		scrd = [int(i) for i in instr[2].split(",")];
		ecrd = [int(i) for i in instr[4].split(",")];
		onGrid(scrd, ecrd);
	elif instr[1] == "off":
		scrd = [int(i) for i in instr[2].split(",")];
		ecrd = [int(i) for i in instr[4].split(",")];
		offGrid(scrd, ecrd);
	elif instr[0] == "toggle":
		scrd = [int(i) for i in instr[1].split(",")];
		ecrd = [int(i) for i in instr[3].split(",")];
		toggleGrid(scrd, ecrd);

def onGrid(scrd, ecrd):
	for x in range(scrd[0], ecrd[0]+1):
		for y in range(scrd[1], ecrd[1]+1):
			bigLights[x][y] = 1;

def offGrid(scrd, ecrd):
	for x in range(scrd[0], ecrd[0]+1):
		for y in range(scrd[1], ecrd[1]+1):
			bigLights[x][y] = 0;

def toggleGrid(scrd, ecrd):
	for x in range(scrd[0], ecrd[0]+1):
		for y in range(scrd[1], ecrd[1]+1):
			if bigLights[x][y] == 0:
				bigLights[x][y] = 1;
			else:
				bigLights[x][y] = 0;

def countOn():
	ocount = 0;
	for x in bigLights:
		for y in x:
			if y == 1:
				ocount += 1;
	return ocount;

for i in inp:
	if i != "":
		parseInstr(i);

print countOn();