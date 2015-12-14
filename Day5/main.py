inp = open('input', 'r').read().split("\n");

def Nice1(inps):
	vcount = 0;
	for i in inps:
		if i in "aeiou":
			vcount += 1;
	if vcount >= 3:
		return True;
	return False;

def Nice2(inps):
	ochar = inps[0]
	for i in range(1, len(inps)):
		if inps[i] == ochar:
			return True;
		ochar = inps[i];
	return False;

def Nice3(inps):
	for i in ["ab","cd","pq","xy"]:
		if i in inps:
			return False;
	return True;

ans = 0;

for i in inp:
	if Nice1(i) and Nice2(i) and Nice3(i):
		ans += 1;

print ans;