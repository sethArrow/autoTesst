from selenium import webdriver
import unittest
import time

PAGE_TITLE='Welcome to Dalex Lender'

class TestDalex(unittest.TestCase):
	def setUp(self):
            self.driver = webdriver.Firefox()
       
        
        def els(self, *args):
	    return [self.driver.find_element_by_name(n) for n in args]
            
        def login(self , username='foo0' , password='bar4'):
            driver =self.driver
            driver.get("http://192.168.0.100:8084")
            self.assertEqual(str(self.driver.title),PAGE_TITLE)
            self.assertIn("Welcome to Dalex Lender",driver.title)
            username, password = self.driver.find_elements_by_name(['username', 'password'])
            self.username.send_keys(username)
            self.password.send_keys(password)
            self.driver.find_element_by_class_name('button').submit()
            
        
        #test valid login
        def test_login(self):
            self.login('foo0','bar4')
            self.assertEqual("http://192.168.0.100:8084/" ,self.driver.current_url)
            self.assertEqual(username.get_attribute('value'),'foo0')
            self.assertEqual(password.get_attribute('value'),'bar4')
            
            

        #test change password
        def test_change_password(self):
            self.login('foo0','bar4')
            self.export=driver.find_element_by_link_text("Settings")
            self.export.click()
            self.change= driver.find_element_by_link_text("Change password")
            self.change.click()
            self.assertEqual("http://192.168.0.100:8084/admin/password_change2/",self.driver.current_url)
            oldpass,newpass,passagain = driver.find_element_by_name(['old_password','new_password1','new_password2'])
            self.submit= driver.find_element_by_class_name('default')
            self.oldpass.send_keys("bar4")
            self.assertEqual(oldpass.get_attribute('value'),'bar4')
            self.newpass.send_keys("bar5")
            self.passagain.send_keys("bar5")
            self.submit.submit()
           
            
        #test the settings feature
        def test_settings(self):
            self.login()
            self.export=driver.find_element_by_link_text("Settings")
            self.export.click()
                
       
        
        #def test_new_client(self):
        #    driver = self.driver
        #    driver.get("http://192.168.0.100:8084")
        #    self.assertIn("Welcome to Dalex Lender",driver.title)
        #    self.username= driver.find_element_by_name('username')
        #    self.password = driver.find_element_by_name("password")
        #    self.submit= driver.find_element_by_class_name('button')
        #    self.username.send_keys("foo0")
        #    self.password.send_keys("bar4")
        #    self.submit.submit()
        #    
        #    self.client=driver.find_element_by_link_text("Clients")
        #    self.client.click()
        #    self.client1=driver.find_element_by_link_text("New Client")
        #    self.client1.click()
        #    
        #    self.title = driver.find_element_name('title')
        #    
            
            
            
            
        
        
if __name__ == '__main__':
    unittest.main()
	
		


