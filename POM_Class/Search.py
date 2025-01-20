from selenium.webdriver.common.by import By


class SearchBox:
    txt_text_id='search_query_top'
    btn_search_name='submit_search'

    def __init__(self,driver):
        self.driver=driver

    def setText(self,text):
        areatxt=self.driver.find_element(By.ID,self.txt_text_id)
        areatxt.send_keys(text)
    def clickBtn(self):
        clickBtn=self.driver.find_element(By.NAME,self.btn_search_name)
        clickBtn.click()