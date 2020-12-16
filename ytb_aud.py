from selenium import webdriver

class music():
    def __init__(self):
        self.driver =  webdriver.Chrome(executable_path=r'C:/Users/kedar/.wdm/drivers/chromedriver/win32/87.0.4280.88/chromedriver.exe')
    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query="+ query)
        video=self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        video.click()

#assist=music()
#assist.play('perfect by one direction')

