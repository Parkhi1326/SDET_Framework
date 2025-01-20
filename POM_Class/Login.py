from selenium.webdriver.common.by import By


class LoginPage:
    txt_useremail_id='email'
    txt_passwd_id='passwd'
    btn_signup_xpath='//*[@id="SubmitLogin"]/span'

    #constructor
    def __init__(self,driver):
        self.driver=driver

        #Actions
    def setUserName(self,username):
        usertxt=self.driver.find_element(By.ID,self.txt_useremail_id)
        usertxt.send_keys(username)
    def setUserPassword(self,password):
        passtxt=self.driver.find_element(By.ID,self.txt_passwd_id)
        passtxt.send_keys(password)
    def clickBtn(self):
        clickBtn=self.driver.find_element(By.XPATH,self.btn_signup_xpath)
        clickBtn.click()