from selenium import webdriver
import unittest
import time
 
class TestDalex(unittest.TestCase):
	def setUp(self):
            self.driver=webdriver.Firefox()
           
        
        def login(self , username , password):
            driver=self.driver
            driver.get("http://192.168.0.100:8084")
            self.assertEqual(str(self.driver.title),'Welcome to Dalex Lender')
            self.assertIn("Welcome to Dalex Lender",driver.title)
            self.username= driver.find_element_by_name('username')
            self.password = driver.find_element_by_name("password")
            self.submit= driver.find_element_by_class_name('button')
            self.username.send_keys(username)
            self.password.send_keys(password)
            self.submit.submit() 
             
        

        def test_valid_login(self):
            driver =self.driver
            self.login('foo0', 'bar')
            self.assertIn()
	    self.assertEqual("http://192.168.0.100:8084/", self.driver.current_url)
        
        
	def test_invalid_login(self):
            driver =self.driver
            self.login('foo0', 'bar2')
	    self.assertTrue("http://192.168.0.100:8084/accounts/login/", self.driver.current_url)        
        
        def test_logout(self):
	    driver = self.driver
            self.login('foo0', 'bar')
            self.link=driver.find_element_by_link_text('Logout')
            self.link.click()
	    self.password = driver.find_element_by_name('password')
            self.username= driver.find_element_by_name('username')
	    self.assertEquals(str(self.username.get_attribute('value')), '')
	    self.assertEquals(str(self.password.get_attribute('value')), '')   
                                                       
        def test_settings(self):
            self.login('foo0','bar')
            driver= self.driver
            self.export=driver.find_element_by_link_text("Settings")
            self.export.click()
            self.assertEqual("http://192.168.0.100:8084/admin/",self.driver.current_url)
            
                
        
        
        def test_new_client_search(self):
            self.login('foo0' ,'bar')
            driver = self.driver
            self.clients= driver.find_element_by_link_text("Clients")
            self.clients.click()
            self.assertEqual("http://192.168.0.100:8084/contacts/",self.driver.current_url)
            self.search = driver.find_element_by_xpath("//input[@type='text']")
            self.search.send_keys('Zinabu')
            
            
           
        def test_active_loans_search(self):
            self.login('foo0','bar')
            driver = self.driver
            self.loans=driver.find_element_by_link_text("Loans")
            self.loans.click()
            self.assertEqual("http://192.168.0.100:8084/loans/",self.driver.current_url)
            self.search = driver.find_element_by_xpath("//input[@aria-controls='data']")
            self.search.send_keys('ABDULAI KOFI')
            #self.assertIn("Welcome to Dalex Lender",driver.title)
            
        
        def test_filter_loans(self):
            self.login('foo0','bar')
            driver = self.driver
            self.loans=driver.find_element_by_link_text("Loans")
            self.loans.click()
            self.assertEqual("http://192.168.0.100:8084/loans/",self.driver.current_url)
            #issue_date,end_date,branch,employer = self.driver.find_element_by_name(['start_date','end_date','branch','employer'])
            self.issue_date = driver.find_element_by_name('start_date')
            self.end_date = driver.find_element_by_name('end_date')
            self.branch = driver.find_element_by_name('branch')
            self.employer = driver.find_element_by_name('employer')
            self.apply = driver.find_element_by_class_name('button')
            self.issue_date.send_keys('2013-08-06')
	    self.end_date.send_keys('2013-08-07')
            self.branch.send_keys('ACCRA')
            self.employer.send_keys('AMA')
            self.apply.submit()
        
        
        def test_admin_login_again(self):
            self.login('foo0','bar')
            driver = self.driver
            self.export=driver.find_element_by_link_text("Settings")
            self.export.click()
            self.assertEqual("http://192.168.0.100:8084/admin/",self.driver.current_url)
            self.change= driver.find_element_by_link_text("Log out")
            self.change.click()
            self.assertEqual("http://192.168.0.100:8084/admin/logout/",self.driver.current_url)
            self.login2 =driver.find_element_by_link_text('Log in again')
            self.login2.click()
            self.password = driver.find_element_by_name('password')
            self.username= driver.find_element_by_name('username')
	    self.assertEquals(str(self.username.get_attribute('value')), '')
	    self.assertEquals(str(self.password.get_attribute('value')), '')
            self.submit= driver.find_element_by_xpath("//input[@type='submit']")
            self.username.send_keys('foo0')
            self.password.send_keys('bar')
            self.submit.submit()
        
        def test_admin_logout(self):
            self.login('foo0','bar')
            driver =self.driver
            self.export=driver.find_element_by_link_text("Settings")
            self.export.click()
            self.assertEqual("http://192.168.0.100:8084/admin/",self.driver.current_url)
            self.change= driver.find_element_by_link_text("Log out")
            self.change.click()
            self.assertEqual("http://192.168.0.100:8084/admin/logout/",self.driver.current_url)
        
            
        def test_add_user(self):
            self.login('foo0','bar')
            driver= self.driver
            self.export=driver.find_element_by_link_text("Settings")
            self.export.click()
            self.assertEqual("http://192.168.0.100:8084/admin/",self.driver.current_url)
            self.users=driver.find_element_by_link_text('Users')
            self.users.click()
        
            self.add_user=driver.find_element_by_link_text('Add user')
            self.add_user.click()
            self.username= driver.find_element_by_name('username')
            self.password= driver.find_element_by_name('password1')
            self.password_again= driver.find_element_by_name('password2')
            self.save= driver.find_element_by_class_name('default')
            self.username.send_keys('seth8')
            self.password.send_keys('nana')
            self.password_again.send_keys('nana')
            self.save.submit()
        
        
        
        
        def test_side_links(self):
            self.login('foo0','bar')
            driver = self.driver
            self.loans =driver.find_element_by_link_text("Loans")
            self.loans.click()
            self.assertEqual("http://192.168.0.100:8084/loans/",self.driver.current_url)
            
            self.clients= driver.find_element_by_link_text("Clients")
            self.clients.click()
            self.assertEqual("http://192.168.0.100:8084/contacts/",self.driver.current_url)
        
       
        def tearDown(self):
            self.driver.close()    
            
        
            
           
            
            
            
            
            
        #def test_change_password(self):
        #    self.login('foo0','bar')
        #    driver =self.driver
        #    self.export=driver.find_element_by_link_text("Settings")
        #    self.export.click()
        #    self.change= driver.find_element_by_link_text("Change password")
        #    self.change.click()
        #    self.assertEqual("http://192.168.0.100:8084/admin/password_change/",self.driver.current_url)
        #    self.oldpass = driver.find_element_by_name("old_password")
        #    self.newpass = driver.find_element_by_name("new_password1")
        #    self.passagain=driver.find_element_by_name("new_password2")
        #    self.submit= driver.find_element_by_class_name("default")
        #    self.oldpass.send_keys("bar")
        #    self.newpass.send_keys("bar1")
        #    self.passagain.send_keys("bar1")
        #    self.submit.submit()    
            
         
            
        
        
        
         
        
        
        
            
            
        
        
if __name__ == '__main__':
    unittest.main()
	
		

