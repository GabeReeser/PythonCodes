#---- Gabriel Reeser ----

def Paycheck(Hours, RPH):
	OVTHours = 0
	OVT = 0
	OVTRPH = 0

	if Hours > 40:
		OVT = Hours - 40
		OVTHours = 1
		OVTRPH = 1.5 * RPH
	total = (Hours * RPH) + (OVTHours * OVT * OVTRPH)

	print('Your total pay is: $'),
	print(total)

Paycheck(30,10)
Paycheck(50,10)
