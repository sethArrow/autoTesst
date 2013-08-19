
from selenium import webdriver
from xvfbwrapper import Xvfb
import unittest

TITLE = 'Welcome to Dalex Lender'
class FormFill(unittest.TestCase):
    
    def setUp(self):
        self.driver=webdriver.Firefox()
    
    def login(self,username,password):
        driver=self.driver
        driver.get("http://192.168.0.100:8084")
        self.assertEqual(str(self.driver.title),TITLE)
        self.assertIn(TITLE , driver.title)
        self.username= driver.find_element_by_name('username')
        self.password = driver.find_element_by_name("password")
        self.submit= driver.find_element_by_class_name('button')
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.submit.submit()
    
    #def testLoanApplication(self):
    #    self.login('foo0','bar')
    #    driver= self.driver
    #    self.export=driver.find_element_by_link_text("Settings")
    #    self.export.click()
    #    self.assertEqual("http://192.168.0.100:8084/admin/",self.driver.current_url)
    #    select =driver.find_element_by_xpath("//select")
    #    all_options=select.find_elements_by_tag_name('option')
    #    for option in all_options:
    #        print "Value is: %s" % option.get_attribute("value")
    #        option.click()
    #    driver.find_element_by_id("submit").click()
        
        
    #def test_search_all_acount(self):
    #    self.login('foo0','bar')
    #    driver=self.driver
    #    self.loans=driver.find_element_by_link_text('Clients')
    #    self.loans.click()
    #    self.search=driver.find_element_by_id('SearchKeywords')
    #    self.assertEquals(str(self.search.get_attribute('value')), 'Search All Accounts')
    #    self.search.send_keys('Zinabu')
    #    
    def test_account_settings(self):
        self.login('foo0','bar')
        driver=self.driver
        self.user= driver.find_element_by_link_text('foo0')
        self.user.click()
        self.fname=driver.find_element_by_name('first_name')
        self.assertEquals(str(self.fname.get_attribute('value')), 'seth')
        self.lname=driver.find_element_by_name('last_name')
        self.assertEquals(str(self.lname.get_attribute('value')), 'amponsah')
        self.email=driver.find_element_by_name('email')
        self.assertEquals(str(self.email.get_attribute('value')), 'samponsah@arrowtesting.com')
        self.password =driver.find_element_by_name('new_password1')
        self.password2=driver.find_element_by_name('new_password2')
        self.password.send_keys('bar')
        self.password2.send_keys('bar')
        driver.find_element_by_xpath("//button[@type='submit']").submit()
    
    def test_quality_check_url(self):
        self.login('foo0','bar')
        driver=self.driver
        driver.find_element_by_link_text("Loans").click()
        driver.find_element_by_xpath("//a[@href='/loans/216/']").click()
        
        
    
    def teardown(self):
        self.browser.quit
        
    
if __name__ == '__main__':
    unittest.main()
    
    



