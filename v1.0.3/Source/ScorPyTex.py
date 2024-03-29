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
	mb.showinfo('Version', '1.0.3')
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
scrlbr = tk.Scrollbar(root)
scrlbr.pack(side = tk.RIGHT, fill = tk.Y)
type_ = tk.Text(root, yscrollcommand = scrlbr.set, width = 500, height = 500)
type_.pack(fill = tk.BOTH)
scrlbr.config(command = type_.yview)
m = tk.Menu(root)
root.config(m = m)
fm = tk.Menu(m)
om = tk.Menu(m)
hm = tk.Menu(m)
m.add_cascade(label = 'File', menu = fm)
m.add_cascade(label = 'Options', menu = om)
m.add_cascade(label = 'Help', menu = hm)
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
fm.add_command(label = 'Compile and show -> Ctrl + R', command = sr)
root.bind('<Control-r>', sr)
fm.add_separator()
fm.add_command(label = 'Exit -> Ctrl + Q', command = ext)
root.bind('<Control-q>', ext)
om.add_command(label = 'Open ScorPyTex Source -> Ctrl + O', command = ss)
root.bind('<Control-o>', ss)
m.add_separator()
m.add_command(label = 'new', command = nw)
m.add_command(label = 'open', command = llld)
m.add_command(label = 'save', command = sssv)
m.add_command(label = 'save as', command = ssv)
m.add_command(label  = 'show pdf', command = sr)
m.add_command(label = 'show log', command = sl)
if len(sys.argv) > 1:
	ld(sys.argv[1])
root.mainloop()
