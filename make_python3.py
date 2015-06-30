import os, re

def make_python3():
	"""This is a script to transform all the solutions into 
	Python 3 solutions."""
	files = os.listdir('exercises')

	exfolder = 'exercises'
	ex3folder = 'exercisespy3'

	if not os.path.exists(ex3folder):
		os.mkdir(ex3folder)

	def converter(file_name):
		with open(exfolder+os.sep+file_name) as f:
			code = f.read()

		py3code = re.sub(r'(print """)(.+) }', r'print("""\2 })', code, 0, re.DOTALL)
		py3code = re.sub(r'(print )(.+) (#.+)', r'print(\2) \3', py3code)
		py3code = re.sub(r'(print )(.+)', r'print(\2)', py3code)

		py3code = re.sub(r'raw_input', r'input', py3code)

		with open(ex3folder+os.sep+file_name, 'w') as f:
			f.write(py3code)

	for f in files:
		if f.endswith('.py'):
			converter(f)
		else:
			os.system('cp {} {}'.format(exfolder+os.sep+f, ex3folder+os.sep+f))

	print('All done!')

if __name__ == '__main__':
	make_python3()
