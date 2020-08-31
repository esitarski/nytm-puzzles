import io
import re

def wordlist():
	yield 'const wordlist = ['
	
	nonAscii = re.compile( r'[^a-z]' )
	first = True
	with open('English (USA).dic', 'rb') as f_in:
		for line in f_in:
			try:
				line = line.decode().strip()
			except:
				continue
			if not nonAscii.search(line) and len(line) == 8:
				yield '{}\n"{}"'.format('' if first else ',', line.upper())
				first = False
	yield '\n];\n'
	
with open('CrazyEightsTemplate.html') as f_in, open('../CrazyEights.html','w') as f_out:
	for line in f_in:
		if '{{wordlist}}' in line:
			for w in wordlist():
				f_out.write( w )
		else:
			f_out.write( line )
