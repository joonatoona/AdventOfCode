inp = open('input', 'r').read().strip("\n");

ans = 0;
for i in inp:
	if i == "(":
		ans += 1;
	if i == ")":
		ans -= 1;

print ans;