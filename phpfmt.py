import sublime, sublime_plugin
import subprocess
import os

class PhpFmtCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		window = sublime.active_window()
		view = self.view
		file_extension = window.extract_variables()['file_extension']
		if file_extension.lower()!='php':
			window.status_message('file not php')
			return
		
		regions = view.sel()
		if len(regions) > 1 or not regions[0].empty():
			for region in view.sel():
				if not region.empty():
					s = view.substr(region)
					view.replace(edit, region, self.format(s))
		else:  # format all text
			alltextreg = sublime.Region(0, view.size())
			s = view.substr(alltextreg)
			view.replace(edit, alltextreg, self.format(s))

	def format(self, text):
		fName='~tmp.php'
		fs=open(fName,"w")
		fs.write(text)
		fs.close()

		sublime.status_message("formating")
		path=os.path.dirname(__file__)

		p=subprocess.Popen("php \"%s\\fmt.php\" -o=- --psr \"%s\""%(path,fName),shell=True,stdout=subprocess.PIPE)
		arr=p.stdout.readlines()
		os.remove(fName)
		ss=''
		for line in arr:
			ss+=str(line.decode("utf8","ignore"))

		if(ss==''):
			raise Exception('check php file is utf-8')

		return ss