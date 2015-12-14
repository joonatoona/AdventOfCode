inp = open('input', 'r').read().strip("\n");

x = 0;
y = 0;
allcoords = [];
trimcoords = [];

for i in inp:
	if i == "^":
		y += 1;
	if i == "v":
		y -= 1;
	if i == "<":
		x -= 1;
	if i == ">":
		x += 1;
	allcoords.append([x,y]);

for i in allcoords:
	if i not in trimcoords:
		trimcoords.append(i);

print len(trimcoords);