def grade(marks, tm):
	g = marks/tm*100
	if 90<g<=100:
		return ("A1")
	elif 80<g<=90:
		return ("A2")
	elif 70<g<=80:
		return ("B1")
	elif 60<g<=70:
		return ("B2")
	elif 50<g<=60:
		return ("C1")
	elif 40<g<=50:
		return ("C2")
	elif 32<g<=40:
		return ("D")
	elif 20<g<=32:
		return ("E1")
	elif 00<=g<=20:
		return ("E2")	

