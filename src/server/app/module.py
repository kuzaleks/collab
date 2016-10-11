def merge(tasks, labs):
	result = {}
	for lab in labs:
		result[lab.num] = []
		for task in tasks:
			if lab.num == task.lab_num: result[lab.num].append(task.num)
	return result

def biggest_lab_length(labs):
	maxi = 0
	for lab in labs:
		if len(labs[lab]) > maxi:
			maxi = len(labs[lab])
	return maxi