from os import system

dep_file = ".dependencies"

def check_dependencies() -> int:
	try:
		with open(dep_file) as f:
			for line in f.readline():
				ret = system(f'pip3 install {line}')
			return ret
	except:
		raise Exception('No .dependencies file',dep_file)
	return -1