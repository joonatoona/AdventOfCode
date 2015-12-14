inp = [i.split("x") for i in open('input', 'r').read().split("\n")];

def calA(l, w, h):
	tmpvar = [l*w, w*h, h*l];
	return tmpvar[0]*2+tmpvar[1]*2+tmpvar[2]*2+min(tmpvar)

ans = 0;

print calA(2,3,4);

for i in inp:
	ans += calA(int(i[0]), int(i[1]), int(i[2]));

print ans;