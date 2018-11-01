import os

from browser import Browser, Element
import pandas as pd



class TestScript(object):

	TESTSHEET_NAME = 'Test'
	OBJECTSSHEET_NAME = 'objects'

	SCREENSHOT_DIR = './screenshot/'


	# Keywords
	OPEN = 'open'
	TYPE = 'type'
	GOTO = 'goto'
	CHECK = 'check'
	CLICK = 'click'
	CLOSE = 'close'	


	def __init__(self, script_loc):


		if not os.path.exists(self.SCREENSHOT_DIR):
			os.mkdir(self.SCREENSHOT_DIR)


		self.script= pd.read_excel(script_loc, self.TESTSHEET_NAME)
		self.objects_sheet = pd.read_excel(script_loc, self.OBJECTSSHEET_NAME)

		self.script = self.script.fillna('')
		self.objects_sheet = self.objects_sheet.fillna('')

	def prepare_objects(self):
		self.objects = {}
		for i, row in self.objects_sheet.iterrows():
			self.objects[row['Name']] = (Element(name=row['name'], id=row['id'], css_selector=row['css_selector'], cls=row['class'], tag=row['tag']))
		return


	def startBrowser(self):
		self.browser = Browser()
		self.browser.open()

	def closeBrowser(self):
		self.browser.close()

	def type(self, obj ,val):
		self.browser.type(obj, val)

	def click(self, obj):
		self.browser.click(obj)

	def check(self, val):
		return self.browser.check_content(val)

	def openUrl(self, url):
		self.browser.openURL(url)


	def validObject(self, obj, isBrowser=False):
		if isBrowser:
			if obj != 'Browser':
				raise Exception("keyword supported only for 'Browser' !")
			return
		if obj not in self.objects.keys():
			raise Exception(obj + ": Invalid Object")


	def screenshot(self, filename):
		self.browser.screenshot(filename)


	def run(self):

		self.prepare_objects()



		for i, row in self.script.iterrows():
			obj = row['Object']
			keyword = row['Keyword']
			val = row['Value']
			mess = row['Message']
			screenshot = (row['Screenshot'] == 'Y' )




			self.validObject(obj, isBrowser=(keyword in ['open', 'close', 'goto', 'check']))

			# switch(keyword):
			if keyword == self.OPEN:
				if obj == 'Browser':
					self.startBrowser()
			elif keyword == self.GOTO:
				if obj == 'Browser':
					self.openUrl(val)
			elif keyword == self.TYPE:
					self.type(self.objects[obj], val)
			elif keyword == self.CLICK:
					self.click(self.objects[obj])
			elif keyword == self.CHECK:
				ret = self.check(val)
				if ret:
					mess += ' - Verified'
				else:
					mess += ' - Not Found'
			elif keyword == self.CLOSE:
				if obj == 'Browser':
					self.closeBrowser()
				else:
					raise Exception('Invalid Request!')
			else:
				raise Exception(keyword+": keyword not found")

			if screenshot:
				self.screenshot(self.SCREENSHOT_DIR+mess+".png")

			print(mess)






if __name__ == '__main__':

	t = TestScript('./scripts/facebook_login.xls')

	t.run()




