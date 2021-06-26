score = input("Enter Score: ")

try: 
	s = float(score)
except:
	print("Error, ingrese un score valido")
	quit()

if s >= 0.0:
	if s <= 1.0:
		if s >= 0.9:
			print("A")
		elif s >= 0.8:
			print("B")
		elif s >= 0.7:
			print("C")
		elif s >= 0.6:
			print("D")
		else:
			print("F")
	else:
		print("Error, ingrese un score entre 0 y 1")
		quit()
else:
		print("Error, ingrese un score entre 0 y 1")
		quit()