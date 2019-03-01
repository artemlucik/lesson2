def life_status(age):
	if age  <7:
		#print('You are in kindergarten')
		status = 'You are in kindergarten'
	elif age in range(7, 19):
		#print ('You are at school')
		status = 'You are at school'		
	elif age in range(18, 26):
		#print ('You are at university')
		status = 'You are at university'
	else:
		#print('You are working')
		status = 'You are working'		
	return	status

try:
	age = int(input('Enter your age:'))
except ValueError:
	print('Please, enter only digits')

if __name__ == '__main__':
	period = life_status(age)
	print(period)