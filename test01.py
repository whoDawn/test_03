# from selenium import webdriver
# import unittest
# class TestDr(unittest.TestCase):
#     def SetUp(self):
#         self.driver=webdriver.Firefox()
#
#         self.driver.get('http://192.168.72.48/iwebshop/')
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#     def test_login(self):
#         self.driver.find_element_by_link_text('登录').click()
#         self.driver.find_element_by_css_selector('[type="text"]').send_keys('admin')
#         self.driver.find_element_by_css_selector('[type="password"]').send_keys('123456')
#         self.driver.find_element_by_link_text('登录').click()
#         self.driver.find_element_by_link_text('安全退出').click()
#     def tearDown(self):
#         self.driver.quit()
# if __name__ == '__main__':
#     unittest.main()





