import os

def makepython3():
	"""This is a script to transform all the solutions into 
	Python 3 solutions."""
	files = os.listdir('exercises')

	exfolder = 'exercises'
	ex3folder = 'exercisespy3'

	if not os.path.exists(ex3folder):
		os.mkdir(ex3folder)

	for f in files:
		os.system('cp {} {}'.format(exfolder+os.sep+f, ex3folder+os.sep+f))
		if f.endswith('.py'):
			os.system('2to3 -w -n --no-diffs {}'.format(ex3folder+os.sep+f))

	print('All done!')

if __name__ == '__main__':
	makepython3()
