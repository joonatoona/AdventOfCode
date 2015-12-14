import hashlib;

inp = open('input', 'r').read().strip("\n");

print inp;

chash = ""
i = 0;

while chash[:5] != "00000":
	i += 1;
	chash = hashlib.md5(inp+str(i)).hexdigest();

print chash;
print i;