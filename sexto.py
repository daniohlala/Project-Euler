def computepay(h,r):
	pay = 0
	pay1 = 0
	pay2 = 0
	aux = 0
	if h > 40:
		aux = h - 40
		pay1 = 40*r
		pay2 = aux*1.5*r
		pay = pay1 + pay2
	else:
		pay = h*r
	return pay

hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter Rate:")
r = float(rph)
p = computepay(h,r)
print("Pay",p)