from selenium import webdriver
import unittest
import time

LOGIN_PAGE_TITLE = 'Welcome to Dalex Lender'

class TestDalex(unittest.TestCase):
	

	def setUp(self):
		self.agent = webdriver.Firefox()
	
	def tearDown(self):
		self.agent.close()

	def els(self, *args):
		return [self.agent.find_element_by_name(n) for n in args]

	def login(self, username='foo3', password='bar'):
		self.agent.get('http://192.168.0.100:8084')
		self.assertEqual(str(self.agent.title), LOGIN_PAGE_TITLE)
		user, passw = self.agent.find_elements_by_name(['username', 'password'])
		user.send_keys(username)
		passw.send_keys(password)
		self.agent.find_element_by_class_name('button').submit()

	def test_login_and_logout(self):
		# login with valid username and password
		self.login()
		self.assertEqual(str(self.agent.title), '')

		#logout 
		logout = self.agent.find_elements_by_tag_name('a')[1]
		logout.click()

		time.sleep(1)

		user, passw = self.els('username', 'password')
		self.assertEqual(user.get_attribute('value'),'')
		self.assertEqual(passw.get_attribute('value'),'')

	def test_invalid_login(self):
		self.login('foo3', 'something')
		self.assertEqual(str(self.agent.title), LOGIN_PAGE_TITLE)

		user, passw = self.els('username', 'password')
		self.assertEqual(user.get_attribute('value'),'foo3')
		self.assertEqual(passw.get_attribute('value'),'')


	# def test_all_links(self):
	# 	agent = self.agent
	# 	agent.get('http://192.168.0.100:8084')

	# 	user, passw = agent.find_element_by_name('username'), agent.find_element_by_name('password')
	# 	user.send_keys('foo')
	# 	passw.send_keys('bar')
	# 	agent.find_element_by_class_name('button').submit()


	# 	for link in agent.find_elements_by_tag_name('a'):
	# 		link.click()
	# 		self.assertIn(link.text,agent.title)

	def test_change_acc_info(self):
		agent = self.agent
		self.login(agent)

		agent.find_element_by_link_text('foo3').click()

		#self.assertIn('Account',str(agent.title))

		agent.find_element_by_name('first_name').send_keys('kwaw')
		agent.find_element_by_name('last_name').send_keys('tk')
		agent.find_element_by_name('email').send_keys('')
		agent.find_element_by_name('new_password1').send_keys('bar3')
		agent.find_element_by_name('new_password2').send_keys('bar3')

		agent.find_element_by_class_name('button').submit()

		agent.find_element_by_link_text('foo3').click()


		sef.assertEqual(agent.find_element_by_name('first_name').get_attribute('value'),'kwaw')
		sef.assertEqual(agent.find_element_by_name('last_name').get_attribute('value'),'tk')































if __name__ == '__main__':
	unittest.main()










