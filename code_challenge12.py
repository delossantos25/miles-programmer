for i in range(1, 10, 1):
	for z in range(10, i, -1):
		print(" ", end = " ")
	for m in range(i, 0, -1):
		print(m, end = " ")
	for l in range(2, i + 1, 1):
		print(l, end = " ")
	print()