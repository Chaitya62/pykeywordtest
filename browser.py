from selenium import webdriver




class Element(object):

	def __init__(self, name='', cls='', id='', tag='', css_selector=''):
		self.name = name
		self.cls = cls
		self.id = id
		self.tag = tag
		self.css_selector = ''






class Browser(object):

	DRIVER_LOCATION = './driver/chromedriver.exe'

	def __init__(self):
		self.driver = None


	def open(self):
		self.driver = webdriver.Chrome(self.DRIVER_LOCATION)

	def close(self):
		self.driver.close()

	def getElement(self, obj):
		if(obj.name != ''):
			return self.driver.find_element_by_name(obj.name)
		if(obj.id != ''):
			return self.driver.find_element_by_id(obj.id)
		if(obj.cls != ''):
			return self.driver.find_element_by_class_name(obj.cls)
		if(obj.css_selector != ''):
			return self.driver.find_element_by_css_selector(obj.css_selector)
		if(obj.tag != ''):
			return self.driver.find_element_by_tag_name(obj.tag)

		raise Exception('Element not found!')


	def openURL(self, url):
		self.driver.get(url)


	def type(self, obj, text):
		ele = self.getElement(obj)
		ele.send_keys(text)

		return

	def click(self, obj):
		ele = self.getElement(obj)
		ele.click()


	def check_content(self, text):
		if text in self.driver.page_source:
			return True
		else: return False

	def screenshot(self, filename):
		self.driver.save_screenshot(filename)




if __name__ == '__main__':
	
	browser = Browser()
	uname_ele = Element(name='email')
	pass_ele = Element(name='pass')


	login_ele = Element(id='loginbutton')
	browser.open()
	browser.openURL('https://facebook.com')

	# Trying to access BIGHEAD's account XD
	browser.type(uname_ele, "password") 
	browser.type(pass_ele, "password") 
	browser.click(login_ele)
	if(browser.check_content('Write something here')):
		print("Logged in ......")
	else:
		print("Log in failed.")
	browser.close()