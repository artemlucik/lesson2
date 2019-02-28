def get_summ(num_one, num_two):
	try:
		return int(num_one) + int(num_two)
	except ValueError:
		return 'Please, enter integer'


summ = get_summ('56',7)
print(summ)