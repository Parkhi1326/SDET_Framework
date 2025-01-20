from selenium.webdriver.common.by import By

class ContactUS:
    txt_email_name='from'
    txt_ref_id='id_order'
    btn_send_name='submitMessage'

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        emailtxt=self.driver.find_element(By.NAME,self.txt_email_name)
        emailtxt.send_keys(email)
    def setRef(self,refrence):
        reftxt=self.driver.find_element(By.ID,self.txt_ref_id)
        reftxt.send_keys(refrence)
    def clickBtn(self):
        clickBtn=self.driver.find_element(By.NAME,self.btn_send_name)
        clickBtn.click()