# num to num
def merge(tasks, labs):
	result = {}
	for lab in labs:
		result[lab.num] = []
		for task in tasks:
			if lab.num == task.lab_num: result[lab.num].append(task.num)
	return result

# obj to obj
def merge_obj(tasks, labs):
	result = {}
	for lab in labs:
		result[lab] = []
		for task in tasks:
			if lab.num == task.lab_num: result[lab].append(task)
	return result

def biggest_lab_length(labs):
	maxi = 0
	for lab in labs:
		if len(labs[lab]) > maxi:
			maxi = len(labs[lab])
	return maxi