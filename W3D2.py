#---- Gabriel Reeser ----

Hours = int(input("Please enter the number of hours: "))
RPH = int(input("Please enter the rate per hour: "))
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

