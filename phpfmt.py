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

		p=subprocess.Popen("php \"%s\\fmt.php\" \"%s\""%(path,file),shell=True)
		p.wait()
		sublime.status_message("success")
