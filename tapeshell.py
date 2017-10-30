import subprocess
import sys


class File(object):
	def __init__(self, args):
		self.args = args
	def command(self, l):
		subprocess.call(l, shell=False)
	def create(self):
		self.command(["touch", self.args])
	def delete(self):
		self.command(["rm", self.args])
	def rename(self, new_name):
		self.command(["mv", self.args, new_name])
	def update(self):
		self.command(["vi", self.args])
	def read(self):
		self.command(["cat", self.args])
	def hlink(self, link_name):
		self.command(["ln", self.args, link_name])
	def slink(self, link_name):
		self.command(["ln", "-s", self.args, link_name])
	def list(self):
		if self.args == None:
			self.command("ls")
		else:
			self.command(["ls", self.args])
	def exit(self):
		self.__del__
		sys.exit(1)
	def __del__(self):
		pass

class History(object):
	def __init__(self):
		pass
	def update(self, cmd):
		with open("db.txt", 'a') as f:
			f.write(cmd+"\n")
	def retrieve(self):
		with open("db.txt", 'r') as f:
			for i in f:
				print i

def main():
	print "Welcome to tapeshell 1.0.0"
	print " "
	flag = True
	h = History()
	while flag:
		c = raw_input("~ ")
		h.update(c)
		com = c.strip().split(" ")
		if len(com) == 1:
			f = File(None)
		else:
			f = File(com[1])
		if com[0] == "create":
			f.create()
		elif com[0] == "delete":
			f.delete()
		elif com[0] == "rename":
			f.rename(com[2])
		elif com[0] == "update":
			f.update()
		elif com[0] == "read":
			f.read()
		elif com[0] == "hlink":
                	f.hlink(com[2])
		elif com[0] == "slink":
                	f.slink(com[2])
		elif com[0] == "list":
			f.list()
		elif com[0] == "exit":
			f.exit()
		elif com[0] == "past":
			h.retrieve()
		else:
			print "Wrong command"


if __name__ == "__main__":
	main()
