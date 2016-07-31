import sublime, sublime_plugin
import subprocess
import os

class PhpFmtCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("formating")
		path=os.path.dirname(__file__)
		file=self.view.file_name()
		if not file:
			sublime.error_message("file not found")
			return

		p=subprocess.Popen("php \"%s\\fmt.php\" -o=- \"%s\""%(path,file),shell=True,stdout=subprocess.PIPE)
		# p.wait()
		ret=p.stdout.readlines()
		ret=map(lambda x:x.decode("utf8","ignore"),ret)
		if(ret==''):
			sublime.error_message("format error check encode is utf8")
			return

		self.view.replace(edit,sublime.Region(0,self.view.size()),"".join(ret))
		sublime.status_message("success")
