import re

name_template = '<h2 class="task-name">{0}</h2>'
paragraph_template = '<p>{0}</p>'

input_test = '<div class="input"><div class="title">Input:</div><pre>'
output_test = '<div class="output"><div class="title">Output:</div><pre>'
test_finish = '</pre></div>'

def task_generate(name, text):
	paragraphs = text.split('\n')
	print paragraphs

	result = name_template.format(name.encode('utf-8'))

	for p in paragraphs:
		p = re.sub('<it>', input_test, p)
		p = re.sub('<ot>', output_test, p)
		p = re.sub('</ft>', test_finish, p)

		if p and p != "\r":
			result += paragraph_template.format(re.sub('</?.t*>', '', p).encode('utf-8'))

	return result


def task_regenerate(text):
	text = text.decode('utf-8')
	name = re.findall('<h2 class="task-name">(.*)</h2>', text.encode('utf-8'))[0]

	text = re.sub('<h2 class="task-name">(.*)</h2>', '', text)
	text = re.sub('<p>', '', text)
	text = re.sub('</p>', '\n', text)
	text = re.sub('<div class="input">', '<it>', text)
	text = re.sub('<div class="output">', '<ot>', text)
	text = re.sub('<div class="title">...?put:</div>', '', text)
	text = re.sub('<pre>', '', text)
	text = re.sub('</pre>', '</ft>', text)
	text = re.sub('<.?div>', '', text)

	
	return name, text
