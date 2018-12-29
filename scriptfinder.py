
import os
from os import walk


def main():
	print('------------------------------')
	cwd = os.getcwd()
	files = []
	for (dirpath, dirnames, filenames) in walk(cwd):
		for file in filenames:
			if file.endswith(".html"):
				files.append(file)
	
				
	
	for file in files:	
		found, where = hasScript(file)
		if found:
			print('')
			print('Script in %s line' % file)
			for line in where:
				print(line)
		
	print('DONE')
	print('------------------------------')
	
	
def hasScript(fileName):  # returns bool and line found
	found = False
	foundOn = []

	file = open(fileName, 'r', encoding="utf8")
	lines = file.readlines()
	for line in range(1, len(lines)+1):
		if "<script>" in lines[line - 1]:
			found = True
			foundOn.append(line)
	return found, foundOn
	

if __name__ == '__main__':
	main()