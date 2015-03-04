height = raw_input("How many inches tall are you?(not feet. numbers only.): ")
weight = raw_input("How many pounds do you weigh?(numbers only): ")

heightint = float(height)
weightint = float(weight)
bmi = (weightint / (heightint ** 2)) * 703
over_bmi = int((24.9 / 703) * (heightint ** 2))
under_bmi = int((18.5 / 703) * (heightint **2))

if bmi < 18:
	print 'You are under weight in a way that could be impacting your health according to bmi standards.'
	print 'A healthy weight for your height is %r.' % under_bmi 
elif bmi < 18.5:
	print 'You are under weight according to bmi standards.'
	print 'A healthy weight for your height is %r.' % under_bmi 
elif bmi < 24.9:
	print 'You are a healthy weight according to bmi standards.'
elif bmi < 29.9:
	print 'You are over weight according to bmi standards.'
	print 'A healthy weight for your height is %r.' % over_bmi 
elif bmi > 30:
	print 'You are over weight in a way that could be impacting your health according to bmi standards.'
	print 'A healthy weight for your height is %r.' % over_bmi

