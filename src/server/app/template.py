name_template = '<h2 class="task-name">{0}</h2>'
paragraph_template = '<p>{0}</p>'

def task_generate(name, text):
	paragraphs = text.split('\n')

	result = name_template.format(name.encode('utf-8'))

	for p in paragraphs:
		result += paragraph_template.format(p.encode('utf-8'))

	return result

