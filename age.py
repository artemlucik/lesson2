def life_status(age):
	if age  <7:
		#print('You are in kindergarten')
		status = 'You are in kindergarten'
	elif age >= 7 and age <=18:
		#print ('You are at school')
		status = 'school'		
	elif age >18 and age <=25:
		#print ('You are at university')
		status = 'You are at university'
	else:
		#print('You are working')
		status = 'You are working'		
	return	status

try:
	age = int(input('Enter your age:'))
	period = life_status(age)
	print(period)
except ValueError:
	print('Please, enter only digits')

