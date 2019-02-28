school = [{'school_class':'4a', 'scores': [3,4,4,5,2]},
		  {'school_class':'4b', 'scores': [5,4,3,3,2]},
		  {'school_class':'4c', 'scores': [5,5,3,5,2]},
		  {'school_class':'4d', 'scores': [5,4,5,5,4]}
		 ]

'''
average_class_score = []

for s in school:
	average_score = sum(s['scores'])/len(s['scores'])
	average_class_score.append(average_score)
	print (f'Average score of class:{s["school_class"]} - {average_score}')
'''

average_class_score = [sum(s['scores'])/len(s['scores']) for s in school]

for s, score in zip(school, average_class_score):
	print (f'Average score of class:{s["school_class"]} - {score}')

average_school_score = sum(average_class_score)/len(average_class_score)
print(f'Average score of school  - {average_school_score}')