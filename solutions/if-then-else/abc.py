line1 = input()
line2 = input()
stringvalues = line1.split()
A = int(stringvalues[0])
B = int(stringvalues[1])
C = int(stringvalues[2])
if B<A:
	A,B = B,A
if (C<B):
	B,C = C,B
	if B<A:
		A,B = B,A
values = {}
values["A"] = A
values["B"] = B
values["C"] = C

print(values[line2[0]], values[line2[1]], values[line2[2]])