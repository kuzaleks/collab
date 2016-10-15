name_template = '<h2 class="task-name">{0}</h2>'
paragraph_template = '<p>{0}</p>'

def task_generate(name, text):
	paragraphs = text.split('\n')

	result = name_template.format(name)

	for p in paragraphs:
		result += paragraph_template.format(p)

	return result

