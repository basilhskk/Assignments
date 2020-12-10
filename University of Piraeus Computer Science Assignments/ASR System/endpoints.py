def endpoints(Er, Zr, ITU, ITR, IZCT):
	# Stage 1
	Le = len(Er)

	#Stage 1
	flag, c, B1 = 1, 0, 1
	while flag:
		while Er[c] <= ITR: c = c + 1
		B1, flag = c, 0

		for c in range(B1 + 1, B1 + 4):
			if c > Le:
				break

			if Er[c] < ITU:
				flag = 1
				break

		if flag:
			c = B1 + 1
		else:
			break

	# Stage 2
	flag, c, E1 = 1, len(Er)-1, c

	while flag:
		while Er[c] <= ITR: c = c - 1

		flag, E1 = 0, c

		for c in range(E1 - 1, E1 - 4, -1):
			if c < 1:
				break

			if Er[c] < ITU:
				flag = 1
				break

		if flag:
			c = E1 - 1
		else:
			break

	# Stage 3
	sumZ = 0
	ind = []

	for i in range(B1, B1 - 26, -1):
		if i < 1:
			break

		if Zr[i] > IZCT:
			sumZ = sumZ + 1
			ind = [i] + ind

	if sumZ >= 4:
		B2 = ind[1]
	else:
		B2 = B1

	# Stage 4
	sumZ = 0
	ind = []

	for i in range(E1, E1 + 26):
		if i > Le:
			break

		if Zr[i-1] > IZCT:
			sumZ = sumZ + 1
			ind = ind + [i]

	if sumZ >= 4:
		E2 = ind[-1]
	else:
		E2 = E1

	# Stage 5
	i = B2 - 1

	while True:
		if i < 1:
			i = 1
			break

		if Er[i] > ITR:
			B2 = i
		else:
			break

		i = i - 1

	i = E2 + 1

	while True:
		if i > Le:
			i = Le
			break

		if Er[i] > ITR:
			E2 = i
		else:
			break

		i = i + 1

	return B2, E2, B1, E1
