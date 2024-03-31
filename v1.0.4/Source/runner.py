import os
def run(shell):
	shell = shell + ' > /dev/null 2>&1 &'
	exec(compile('os.system(shell)', 'file', 'exec'))