import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import os
from os import path
from runner import run
import sys
import getpass
if sys.platform != 'linux':
	sys.exit()
root = tk.Tk()
try:
	image = tk.PhotoImage(file = '/usr/share/ScorPyTex/Icon.png')
except:
	try:
		image = tk.PhotoImage(file = 'Icon.png')
	except:
		mb.showerror('Error', 'Icon.png was not found')
		sys.exit()
root.geometry('650x500')
root.iconphoto(False, image)
root.title('ScorPyTex')
title = ''
def ScorPyon():
	old = os.getcwd()
	try:
		os.chdir('/usr/share/ScorPyon/')
	except:
		return False
	else:
		os.chdir(old)
		return True
def ss(event = None):
	answer = mb.askquestion('Warning', 'Are you sure you want to close this document ?', icon = 'warning')
	if answer == 'yes':
		if not ScorPyon():
			ld('/usr/share/ScorPyTex/ScorPyTex.py')
		elif mb.askquestion('Question', 'ScorPyon is installed on this system. Do you want to open the python file in ScorPyon ?', icon = 'info') == 'yes':
			os.system('ScorPyon /usr/share/ScorPyTex/ScorPyTex.py')
		else:
			ld('/usr/share/ScorPyTex/ScorPyTex.py')
def shv(event = None):
	mb.showinfo('Version', '1.0.4')
def rafey(event = None):
	mb.showinfo('Author', 'Rafey <https://github.com/rafugafu>')
def lld():
	fn = fd.askopenfilename(initialdir = f'/home/{getpass.getuser()}/', title = 'Open', filetypes = (('Tex Files', '*.tex'), ('All Files', '*.*')))
	ld(fn)
def ssssv(nm):
	if not nm == '':
		file = open(nm, 'w')
		file.writelines(type_.get(1.0, 'end'))
		file.close()
	clt(nm)
def clt(nt):
	global title
	try:
		if not nt == '':
			root.title('ScorPyTex' + ' - ' + nt)
		else:
			root.title('ScorPyTex')
		title = nt
	except:
		pass
	else:
		h()
def sssv(event = None):
	global title
	if not title == '':
		ssssv(title)
	else:
		ssv()
def asktex():
	while True:
		ans = str(sd.askstring('Select Compiler', prompt = 'Type either [pdflatex, lualatex]:')).lower().replace(' ', '')
		if ans in ['pdflatex', 'lualatex']:
			break
		else:
			mb.showerror('Error', 'That is not a valid option')
	return ans
def pdf(title):
	if title[len(title) - 3:] == 'tex':
		pdf_ = title[:-4]
	else:
		pdf_ = title
	pdf_ = path.basename(pdf_) + '.pdf'
	if not path.exists(pdf_):
		mb.showerror('Error', 'There is an error in your code.')
		sl()
		return
	try:
		os.system('xdg-open ' + pdf_.replace(' ', '\ '))
	except Exception as error:
		mb.showerror('Error', error)
def runtex(compiler):
	global type_
	global title
	compiler = compiler + 'latex '
	run(compiler + title.replace(' ', '\ '))
	pdf(title)
def sr(event = None):
	tex = asktex()
	if not title:
		mb.showerror('Error', 'Blank document')
		return
	sv(title)
	if tex == 'lualatex':
		runtex('lua')
	elif tex == 'pdflatex':
		runtex('pdf')
def ext(event = None):
	global root
	answer = mb.askquestion('Warning', 'Are you sure you want to exit ?', icon = 'warning')
	if answer == 'yes':
		root.destroy()
def ld(nm):
	global type_
	global root
	if not nm == '':
		try:
			file = open(nm, 'r')
			lines = file.readlines()
			type_.delete('1.0', 'end')
			for i in range(len(lines)):
				type_.insert(tk.END, lines[i])
			file.close()
		except Exception as error:
			mb.showerror('Error', error)
		else:
			os.chdir(path.dirname(nm))
	clt(nm)
def llld(event = None):
	answer = mb.askquestion('Warning', 'Are you sure you want to close this document ?', icon = 'warning')
	if answer == 'yes':
		lld()
def sv(nm):
	global root
	if not nm == '':
		try:
			file = open(nm, 'w')
			file.writelines(type_.get(1.0, 'end'))
			file.close()
			clt(nm)
		except:
			pass
def ssv(event = None):
	fn = fd.asksaveasfilename(initialdir = f'/home/{getpass.getuser()}/', title = 'Save', filetypes = (('Tex Files', '*.tex'), ('All Files', '*.*')))
	sv(fn)
	clt(fn)
def nw(event = None):
	answer = mb.askquestion('Warning', 'Are you sure you want to open a new document ?', icon = 'warning')
	if answer == 'yes':
		type_.delete('1.0', 'end')
		clt('')
def sl_(name_):
	win = tk.Tk()
	win.title(name_)
	log = tk.Text(win, height = 500, width = 500)
	log.pack(fill = tk.BOTH)
	log.insert('1.0', open(name_, 'r').read())
	log.configure(state = 'disabled')
	win.mainloop()
def sl(event = None):
	if title[len(title) - 3:] == 'tex':
		name_ = title[:-4]
	else:
		name_ = title
	name_ = path.basename(name_) + '.log'
	if path.exists(name_):
		sl_(name_)
	else:
		mb.showinfo('Info', 'The log file does not exist')
def hc():
	global type_
	type_.tag_remove('comment', '1.0', 'end')
	n = '1.0'
	searchstr = r'%.+?\n'
	while True:
		count = tk.IntVar()
		n = type_.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
		if not n: break
		nn = '%s+%dc' % (n, count.get())
		type_.tag_add('comment', n, nn)
		n = nn
	type_.tag_config('comment', foreground = 'grey')
def hm_():
	global type_
	type_.tag_remove('math', '1.0', 'end')
	n = '1.0'
	search = r'\$.+?\$'
	while True:
		count = tk.IntVar()
		n = type_.search(search, n, nocase = 1, count = count, stopindex = 'end', regexp = True)
		if not n: break
		nn = '%s+%dc' % (n, count.get())
		type_.tag_add('math', n, nn)
		n = nn
	type_.tag_config('math', foreground = 'red')
def hs():
	global type_
	type_.tag_remove('slash', '1.0', 'end')
	n = '1.0'
	search = r'\\.+?\ '
	while True:
		count = tk.IntVar()
		n = type_.search(search, n, nocase = 1, count = count, stopindex = 'end', regexp = True)
		if not n: break
		nn = '%s+%dc' % (n, count.get())
		type_.tag_add('slash', n, nn)
		n = nn
	n = '1.0'
	search = r'\\.+?\{'
	while True:
		count = tk.IntVar()
		n = type_.search(search, n, nocase = 1, count = count, stopindex = 'end', regexp = True)
		if not n: break
		nn = '%s+%dc' % (n, count.get())
		type_.tag_add('slash', n, nn)
		n = nn
	type_.tag_config('slash', foreground = 'magenta')
def hcb():
	global type_
	type_.tag_remove('cbracket', '1.0', 'end')
	n = '1.0'
	search = r'\{.+?\}'
	while True:
		count = tk.IntVar()
		n = type_.search(search, n, nocase = 1, count = count, stopindex = 'end', regexp = True)
		if not n: break
		nn = '%s+%dc' % (n, count.get())
		type_.tag_add('cbracket', n, nn)
		n = nn
	type_.tag_config('cbracket', foreground = 'blue')
def hsb():
	global type_
	type_.tag_remove('sbracket', '1.0', 'end')
	n = '1.0'
	search = r'\[.+?\]'
	while True:
		count = tk.IntVar()
		n = type_.search(search, n, nocase = 1, count = count, stopindex = 'end', regexp = True)
		if not n: break
		nn = '%s+%dc' % (n, count.get())
		type_.tag_add('sbracket', n, nn)
		n = nn
	type_.tag_config('sbracket', foreground = 'brown')
def h(event = None):
	hm_()
	hc()
	hs()
	hcb()
	hsb()
def fr(event = None):
	global type_
	find = sd.askstring('Find & Replace', prompt = 'Text to Find:')
	replace = sd.askstring('Find & Replace', prompt = 'Replace with:')
	if find != '' and find != None and replace != None:
		n = '1.0'
		search = r'\y' + find + r'\y'
		while True:
			n = type_.search(search, n, nocase = 1, stopindex = 'end', regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, len(find))
			type_.delete(n, nn)
			type_.insert(n, replace)
			n = nn
def f(event = None):
	global type_
	find = sd.askstring('Find', prompt = 'Text to Find:')
	if find != '' and find != None:
		type_.tag_remove('found', '1.0', 'end')
		n = '1.0'
		search = r'\y' + find + r'\y'
		while True:
			n = type_.search(search, n, nocase = 1, stopindex = 'end', regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, len(find))
			type_.tag_add('found', n, nn)
			n = nn
		type_.tag_config('found', foreground = 'white', background = 'black')
	if find == '':
		type_.tag_remove('found', '1.0', 'end')
scrlbr = tk.Scrollbar(root)
scrlbr.pack(side = tk.RIGHT, fill = tk.Y)
type_ = tk.Text(root, yscrollcommand = scrlbr.set, width = 500, height = 500)
type_.pack(fill = tk.BOTH)
type_.bind('<KeyRelease>', h)
scrlbr.config(command = type_.yview)
m = tk.Menu(root)
root.config(m = m)
fm = tk.Menu(m)
em = tk.Menu(m)
om = tk.Menu(m)
hm = tk.Menu(m)
m.add_cascade(label = 'File', menu = fm)
m.add_cascade(label = 'Edit', menu = em)
m.add_cascade(label = 'Options', menu = om)
m.add_cascade(label = 'Help', menu = hm)
em.add_command(label = 'Find -> Ctrl + F', command = f)
root.bind('<Control-f>', f)
em.add_command(label = 'Find & Replace -> Ctrl + Shift + F', command = fr)
root.bind('<Control-F>', fr)
hm.add_command(label = 'Version', command = shv)
hm.add_command(label = 'Author', command = rafey)
fm.add_command(label = 'New -> Ctrl + N', command = nw)
root.bind('<Control-n>', nw)
fm.add_command(label = 'Open -> Ctrl + L', command = llld)
root.bind('<Control-l>', llld)
fm.add_separator()
fm.add_command(label = 'Save -> Ctrl + S', command = sssv)
root.bind('<Control-s>', sssv)
fm.add_command(label = 'Save as -> Ctrl + Shift + S', command = ssv)
root.bind('<Control-S>', ssv)
fm.add_command(label = 'Compile and show -> Ctrl + R', command = sr)
root.bind('<Control-r>', sr)
fm.add_command(label = 'Show Log', command = sl)
fm.add_separator()
fm.add_command(label = 'Exit -> Ctrl + Q', command = ext)
root.bind('<Control-q>', ext)
om.add_command(label = 'Open ScorPyTex Source -> Ctrl + O', command = ss)
root.bind('<Control-o>', ss)
m.add_separator()
m.add_command(label  = 'show pdf', command = sr)
m.add_command(label = 'show log', command = sl)
if len(sys.argv) > 1:
	ld(sys.argv[1])
root.mainloop()
