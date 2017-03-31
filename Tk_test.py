#coding:utf-8

from Tkinter import *

class Application(Frame):
	def say_hi(self):
		print "Hi there everyone!"

	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "Quit"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit

		self.QUIT.pack({"side":"left"})

		self.hi_there = Button(self)
		self.hi_there["text"] = "Hello"
		self.hi_there["command"] = self.say_hi

		self.hi_there.pack({"side":"left"})

		self.entrythingy = Entry()
		self.entrythingy.pack()

		self.contents = StringVar()
		self.contents.set("This is a variable")
		self.entrythingy["textvariable"] = self.contents

		self.entrythingy.bind('<Key-Return>', self.print_contents)

		self.upload_code = Text(self)
		# self.upload_code["text"] = "The code you want to upload!"
		self.upload_code.pack()

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def print_contents(self, event):
		print "hi. contents of entry is now ----->",\
				self.contents.get()

root = Tk()
app = Application(master = root)
app.master.title("My Do-Nothing Application")
app.master.maxsize(1200, 800)
app.mainloop()
root.destroy()