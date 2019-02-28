def comperasion(string_1,string_2):
	if type(string_1) != str or type(string_2) != str:
		#print ('0')
		return 0
	elif string_1 == string_2:
		#print('1')
		return 1
	elif len(string_1) > len(string_2):
		#print('2')
		return 2
	elif string_2 == 'learn':
		#print('3')
		return 3

str_1 = 'test'
str_2 = 'learn'

print(comperasion(str_1,str_2))